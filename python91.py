from datetime import date
print(f'\033[1mCADASTRO DE TRABALHADORES\033[m')
cidadoes = list()
while True:
    cidadao = dict()
    cidadao['Nome:'] = input('\nNome: ')
    nascimento = int(input(f'Ano de nascimento de {cidadao["Nome:"]}: '))
    cidadao['Idade:'] = date.today().year - nascimento
    cidadao['Carteira de trabalho:'] = int(input(f'N.º da carteira de trabalho de {cidadao["Nome:"]} (0 se não tiver): '))
    if cidadao['Carteira de trabalho:'] == 0:
        cidadao['Carteira de trabalho:'] = '0 anos de contribuição, ainda não possuí.'
        cidadoes.append(cidadao.copy())
    else:
        aContratacao = int(input(f'Ano de contratação de {cidadao["Nome:"]}: '))
        tContribuicao = date.today().year - aContratacao
        cidadao['Salário: R$'] = float(input(f'Salário de {cidadao["Nome:"]}: R$'))
        cidadao['Idade da aposentadoria:'] = cidadao['Idade:'] + (35 - tContribuicao)
        cidadoes.append(cidadao.copy())
    c = input('Deseja continuar informando mais pessoas (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar informando mais pessoas (S/N)? ').strip()[0]
    if c in 'nN':
        break
print(f'\n\033[1m{"Todos cidadões cadastrados e suas aposentadorias":^60}\033[m')
for cidadao in cidadoes:
    print('=-'*30)
    for k, v in cidadao.items():
        print(f'{k} {v}')

# suponha apenas a condição de 35 anos de trabalho para se aposentar (kkkk)
