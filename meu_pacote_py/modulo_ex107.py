# arquivo usado como modulo referente ao exercício 107, uma modularização do python107.py


def dobro(f=0.0):
    """
    ->Função que fornece o dobro de um número.
    :param f: float de entrada
    :return: float que é o dobro do float de entrada
    """
    return 2*f


def metade(f=0.0):
    """
    ->Função que fornece a metade de um número.
    :param f: float de entrada
    :return: float que é a metade do float de entrada
    """
    return 0.5*f


def aumentar(f=0.0, a=0.0):
    """
    ->Função que fornece um número aumentado por um determinado acréscimo porcentual.
    :param f: float que representa o número a receber um acréscimo porcentual
    :param a: float que representa o acréscimo porcentual
    :return: float que é o parametro f acrescido porcentualmente pelo parametro a
    """
    return (1+(a/100))*f


def diminuir(f=0.0, d=0.0):
    """
    ->Função que fornece um número diminuído por um determinado descréscimo porcentual.
    :param f: float que representa o número a receber um descréscimo porcentual
    :param d: float que representa o descréscimo porcentual
    :return: float que é o parametro f descrescido porcentualmente pelo parametro a
    """
    return (1-(d/100))*f


def moeda(f=0.0, m='US$'):
    """
    ->Função que formata um número em forma monetária de acordo com a unidade monetário (dolár por padrão).
    :param f: float que representa o número a ser formatado em forma monetária
    :param m: string referente a unidade monetária, por padrão é a string 'US$'
    :return: string que representa o número formatado em forma monetária
    """
    return f'{m}{f:.2f}'.replace('.', ',')
