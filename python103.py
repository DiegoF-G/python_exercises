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


while True:
    inteiro = leia_int('Digite um número inteiro: ')
    print(f'Você acabou de digitar o inteiro {inteiro}.')
    r = input('Continuar digitando números inteiros (S/N)? ').strip()[0]
    while r not in 'sSnN':
        r = input('Continuar digitando números inteiros (S/N)? ').strip()[0]
    if r in 'nN':
        break
help(leia_int)
