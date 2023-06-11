# pack referente ao exercício 110, e tambem será usado em outros


def leia_dinheiro(d):
    """
    ->Função que valida ("por cima", é uma validação incompleta) e amarzena a entrada de valores monetários.
    :param d: string, que representa o float a ser convertido
    :return: float, que representa a quantia monetária inserida
    """
    x = input(d)
    while x.isalpha() or x.isspace() or x == '':
        print('\033[0:31mPreço inválido, digite novamente.\033[m')
        x = input(d)
    return float(x.replace(',', '.'))









