import re

def phone_validator(phone: str) -> bool:
    regex = re.compile(r"^\(\d{2}\)\s9?\d{4}-\d{4}$")
    return bool(regex.match(phone))
    
    
def remove_characters(cnpj: str) -> str:
    format_cnpj = ''.join(filter(str.isdigit, str(cnpj)))
    return format_cnpj.zfill(14)


def calculate_digit(cnpj: str, weight: int) -> str:
    total = sum(int(digit) * weight for digit, weight in zip(cnpj, weight))
    rest = total % 11
    return '0' if rest < 2 else str(11 - rest)


def cnpj_validator(cnpj: str) -> bool:
    cnpj = remove_characters(cnpj)
    # if len(cnpj) != 14 or len(set(cnpj)) == 1:
    #     return False

    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = calculate_digit(cnpj[:12], pesos_1)

    pesos_2 = [6] + pesos_1
    segundo_digito = calculate_digit(cnpj[:12] + primeiro_digito, pesos_2)

    return cnpj[-2:] == primeiro_digito + segundo_digito


def email_validator(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))