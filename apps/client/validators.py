import re
from validate_docbr import CPF


def valid_number(field, number):
    return len(field) == number


def valid_cpf(cpf_number):
    cpf = CPF()
    return cpf.validate(cpf_number)


def valid_string(field):
    return field.isalpha()


def valid_celphone(celphone):
    """Verify if celphone have the pattern 00 0000-000"""
    pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    verify = re.findall(pattern, celphone)
    return verify
