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


def leia_int(m='Digite um inteiro: '):
    """
    ->Função que lê um inteiro se, e somente se, a string digitada pode ser convertida no tipo primitivo inteiro.
      No caso de não ser possível essa conversão, é printado uma string informando que o valor é inválido.
    :param m: string, que se espera ser uma mensagem solicitando qual o inteiro em questão
    :return: inteiro, convertido da string se possível a conversão
    """
    while True:
        try:
            n = int(input(m))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__}. Ops! O valor digitado não é um inteiro. Favor digite novamente.\033[m')
        else:
            return n


def leia_float(m='Digite um número real: '):
    """
    ->Função que lê um número real se, e somente se, a string digitada pode ser convertida no tipo primitivo float.
      No caso de não ser possível essa conversão, é printado uma string informando que o valor é inválido.
      Observação: Aceita o uso de vírgula para escrever o ponto flutuante.
    :param m: string, que se espera ser uma mensagem solicitando qual o número real em questão
    :return: float convertido da string, se possível a conversão
    """
    while True:
        try:
            x = float(input(m).replace(',', '.'))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__}. Ops! O valor digitado não é um número real. Favor digite novamente.\033[m')
        else:
            return x

