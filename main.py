import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
import logging

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
    

def save_outputs(path: str, data: list[dict]):
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

    
def extract_data(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        tree = etree.HTML(str(soup))
        data = tree.xpath("//*[@class='inline cursor-copy']/span")
        obj = {
            'Razao Social': data[2].text,
            'Porte': data[3].text,
            'Capital': data[4].text,
            'Natureza Juridica': f'{data[5].text} {data[6].text}',
            'CNPJ': data[9].text,
            'Situacao Cadastral': data[13].text,
            'Telefone': data[15].text,
            'Email': data[16].text,
            'Endereco': f'{data[18].text}, {data[19].text}, {data[20].text}, {data[21].text}, {data[22].text}, {data[23].text}'
        }
        print('Dados extraídos com sucesso')
        return obj
    except Exception as e:
        raise Exception(f'Erro ao extrair os dados: {e}')
    

def main():
    try:
        cnpjs = read_inputs(PATH_INPUTS, COLUMN_INPUTS)
        all_data = []
        for cnpj in cnpjs:
            print(f'Iniciando processo do CNPJ: {cnpj}')
            data = extract_data(f'{URL}{cnpj}')
            all_data.append(data)
            sleep(13)  # Aguardo devido ao número de requisições máximas por minuto no site
        save_outputs(PATH_OUTPUTS, all_data)
    except Exception as e:
        logging.error(e)
        
        
if __name__ == '__main__':
    main()
