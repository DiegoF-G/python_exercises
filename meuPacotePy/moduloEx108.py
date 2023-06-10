# arquivo usado como modulo referente ao exercício 108, uma modularização do python108.py


def dobro(f=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece o dobro de um número.
    :param f: float de entrada
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o dobro do float de entrada
    """
    return 2*f if monetario is False else moeda(2*f, m=unidade)


def metade(f=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece a metade de um número.
    :param f: float de entrada
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é a metade do float de entrada
    """
    return 0.5*f if monetario is False else moeda(0.5*f, m=unidade)


def aumentar(f=0.0, a=0, monetario=False, unidade='US$'):
    """
    ->Função que fornece um número aumentado por um determinado acréscimo porcentual.
    :param f: float que representa o número a receber um acréscimo porcentual
    :param a: float que representa o acréscimo porcentual
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o parametro f acrescido porcentualmente pelo parametro a
    """
    return (1+(a/100))*f if monetario is False else moeda((1+(a/100))*f, m=unidade)


def diminuir(f=0.0, d=0, monetario=False, unidade='US$'):
    """
    ->Função que fornece um número diminuído por um determinado descréscimo porcentual.
    :param f: float que representa o número a receber um descréscimo porcentual
    :param d: float que representa o descréscimo porcentual
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o parametro f descrescido porcentualmente pelo parametro a
    """
    return (1-(d/100))*f if monetario is False else moeda((1-(d/100))*f, m=unidade)


def moeda(f=0.0, m='US$'):
    """
    ->Função que formata um número em forma monetária de acordo com a unidade monetário (dolár por padrão).
    :param f: float que representa o número a ser formatado em forma monetária
    :param m: string referente a unidade monetária, por padrão é a string 'US$'
    :return: string que representa o número formatado em forma monetária
    """
    return f'{m}{f:.2f}'.replace('.', ',')


