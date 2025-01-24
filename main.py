import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH_INPUTS = 'Inputs.xlsx'

def read_inputs(path: str) -> list[int]|None:
    try:
        df = pd.read_excel(path)
        return df['CNPJ']
    except Exception as e:
        raise Exception(f'Erro ao efetuar a leitura da planilha de inputs: {e}')
    
def start_driver():
    try:
        driver = webdriver.Chrome()
        return driver
    except Exception as e:
        raise Exception(f'Erro ao iniciar o navegador: {e}')


def main(path_inputs):
    try:
        cnpjs = read_inputs(path_inputs)
        driver = start_driver()
        for cnpj in cnpjs:
            print(cnpj)
    except Exception as e:
        print(e)
    finally:
        # driver.quit()
        ...
        
        
if __name__ == '__main__':
    main(PATH_INPUTS)