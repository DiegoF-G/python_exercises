def leia_int(m='Digite um inteiro: '):
    """
    ->Função que lê um inteiro se, e somente se, a string digitada pode ser convertida no tipo primitivo inteiro apenas.
      No caso de não ser possível uma conversão, é printado uma string informando que o valor é inválido.
    :param m: string, que se espera ser uma mensagem solicitando qual o inteiro em questão
    :return: inteiro, obtido da string quando a conversão é possível
    """
    while True:
        n = input(m)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0:31mValor inválido! Digite um número inteiro.\033[m')


while True:
    inteiro = leia_int('Digite um número inteiro: ')
    print(f'Você acabou de digitar o inteiro {inteiro}.')
    r = input('Continuar digitando números inteiros (S/N)? ').strip()[0]
    while r not in 'sSnN':
        r = input('Continuar digitando números inteiros (S/N)? ').strip()[0]
    if r in 'nN':
        break
help(leia_int)
