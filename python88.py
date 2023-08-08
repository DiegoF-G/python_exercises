print('\033[1mBOLETIM\033[m')
nomes_notas = []
while True:
    nome_nota = [None, []]
    nome_nota[0] = input('Nome: ')
    nome_nota[1].append(float(input('Nota N1: ')))
    nome_nota[1].append(float(input('Nota N2: ')))
    nomes_notas.append(nome_nota)
    c = input('Deseja continuar digitando mais nomes e notas (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais nomes e notas (S/N)? ').strip()[0]
    if c in 'nN':
        break
t = (print('-='*40), print(f'No.{"Nome":^15}{"Média":^15}'))
for i in range(0, len(nomes_notas)):
    print(f'{i+1} {nomes_notas[i][0]:^15} {(nomes_notas[i][1][0] + nomes_notas[i][1][1]) / 2:^15}')
while True:
    a = int(input('\nMostrar notas de qual pessoa (digite o número correspondente dela, 0 para encerra)? '))
    if 0 < a <= len(nomes_notas):
        print(f'\n{nomes_notas[a-1]}')
    elif a == 0:
        break
print('\n\033[1mPrograma encerrado.\033[m')
