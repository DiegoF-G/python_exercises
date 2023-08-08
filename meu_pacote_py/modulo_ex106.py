# arquivo usado como modulo referente ao exercício 106, uma modularização do python106.py


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