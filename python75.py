listagem = (input('Nome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')),
            input('\nNome do produto: '), float(input('Valor do produto por unidade: R$')))
lista_precos = (print(), print('-'*40), print(f'{"PREÇOS":^38}'), print('-'*40))
for i, l in enumerate(listagem):
    if i % 2 == 0:
        print(f'{l:.<30}', end=' ')
    else:
        print(f'R${l:.2f}')
