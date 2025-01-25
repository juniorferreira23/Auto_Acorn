import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
from validators import phone_validator, cnpj_validator, email_validator

PATH_INPUTS = 'inputs.xlsx'
PATH_OUTPUTS = 'outputs.xlsx'
URL = 'https://cnpja.com/office/'
COLUMN_INPUTS = 'CNPJ'

def read_inputs(path: str, column: str) -> list:
    try:
        df = pd.read_excel(path)
        print('Planilha de Inputs lida com sucesso')
        return df[column].tolist()
    except Exception as e:
        raise Exception(f'Erro ao efetuar a leitura da planilha de inputs: {e}')
    

def save_outputs(path: str, data: list[dict]) -> None:
    try:
        new_data = pd.DataFrame(data)
        try:
            existing_data = pd.read_excel(path)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        except FileNotFoundError:
            updated_data = new_data
        updated_data.to_excel(path, index=False)
        print(f'Dados salvos com sucesso em {path}')
    except Exception as e:
        raise Exception(f'Erro ao salvar os dados: {e}')
    
    
def format_data(data: list[str]):
    increment = 0
    try:
        if cnpj_validator(data[9].text):
            cnpj = data[9].text
        else:
            increment = 1
            cnpj = data[9 + increment].text
            
        if data[13 + increment].text == 'Ativa' or data[13 + increment].text == 'Inapta':
            status = data[13 + increment].text
        elif data[13 + increment - 1].text == 'Ativa' or data[13 + increment -1].text == 'Inapta':
            increment -= 1
            status = data[13 + increment].text
        else:
            increment += 1
            status = data[13 + increment].text
            
        if phone_validator(data[15 + increment].text):
            telefone = data[15 + increment].text
        else:
            increment += 1
            telefone = data[15 + increment].text

        if phone_validator(data[16 + increment].text):
            if email_validator(data[16 + increment + 1].text):
                increment += 1
                email = data[16 + increment].text
            else:
                increment -= 1
                email = ''
        else:
            if email_validator(data[16 + increment].text):
                email = data[16 + increment].text
            elif email_validator(data[16 + increment + 1].text):
                increment += 1
                email = data[16 + increment].text
            elif email_validator(data[16 + increment - 1].text):
                increment -= 1
                email = data[16 + increment].text
            else:
                increment -= 1
                email = ''

        obj = {
            'Razao Social': data[2].text,
            'Porte': data[3].text,
            'Capital': data[4].text,
            'Natureza Juridica': f'{data[5].text} {data[6].text}',
            'CNPJ': cnpj,
            'Situacao Cadastral': status,
            'Telefone': telefone,
            'Email': email,
            'Endereco': f'{data[18 + increment].text}, '
                        f'{data[19 + increment].text}, '
                        f'{data[20 + increment].text}, '
                        f'{data[21 + increment].text}, '
                        f'{data[22 + increment].text}, '
                        f'{data[23 + increment].text}'
        }
        return obj
    except Exception as e:
        raise Exception(f'Erro ao formatar dados extraídos: {e}')

    
def extract_data(url) -> object:
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        tree = etree.HTML(str(soup))
        data = tree.xpath("//*[@class='inline cursor-copy']/span")
        print('Dados extraídos com sucesso')
        return data
    except Exception as e:
        raise Exception(f'Erro ao extrair os dados: {e}')
    

def main():
    try:
        cnpjs = read_inputs(PATH_INPUTS, COLUMN_INPUTS)
        all_data = []
        for cnpj in cnpjs:
            if cnpj_validator(cnpj):                
                print(f'Iniciando processo do CNPJ: {cnpj}')
                data = extract_data(f'{URL}{cnpj}')
                obj = format_data(data)
                all_data.append(obj)
                sleep(13)  # Aguardo devido ao número de requisições máximas por minuto no site
            else:
                obj = {'Razao Social': 'CNPJ INVÁLIDO', 'CNPJ': cnpj}
                all_data.append(obj)
        save_outputs(PATH_OUTPUTS, all_data)
    except Exception as e:
        print(e)
        
        
if __name__ == '__main__':
    main()
