# pack referente ao exercício 110, e tambem será usado em outros


def leia_dinheiro(d):
    """
    ->Função que valida ("por cima", é uma validação incompleta) e amarzena a entrada de dados monetários.
    :param d: uma string a ser convertida em float, se possível
    :return: float que representa a quantia monetária inserida
    """
    x = input(d)
    while x.isalpha() or x.isspace() or x == '':
        print('\033[0:31mValor inválido, digite novamente.\033[m')
        x = input(d)
    return float(x.replace(',', '.'))


def leia_int(m='Digite um inteiro: '):
    """
    ->Função que lê um inteiro se, e somente se, a string digitada pode ser convertida em apenas no tipo primitivo inteiro.
      No caso de não ser possível uma conversão, é printado uma string informando que o valor é inválido.
    :param m: uma string qualquer
    :return: um inteiro obtido da string dada pelo parâmetro
    """
    while True:
        n = input(m)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0:31mValor inválido! Digite um número inteiro.\033[m')






