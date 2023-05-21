print('\033[1mBOLETIM\033[m')
nomesNotas = []
while True:
    nomeNota = [None, []]
    nomeNota[0] = input('Nome: ')
    nomeNota[1].append(float(input('Nota N1: ')))
    nomeNota[1].append(float(input('Nota N2: ')))
    nomesNotas.append(nomeNota)
    c = input('Deseja continuar digitando mais nomes e notas (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais nomes e notas (S/N)? ').strip()[0]
    if c in 'nN':
        break
t = (print('-='*40), print(f'No.{"Nome":^15}{"Média":^15}'))
for i in range(0, len(nomesNotas)):
    print(f'{i+1} {nomesNotas[i][0]:^15} {(nomesNotas[i][1][0] + nomesNotas[i][1][1]) / 2:^15}')
while True:
    a = int(input('\nMostrar notas de qual pessoa (digite o número correspondente dela, 0 para encerra)? '))
    if a < len(nomesNotas):
        print(f'\n{nomesNotas[a-1]}')
    elif a > len(nomesNotas) or a < 0:
        a = int(input('\nMostrar notas de qual pessoa (digite o número correspondente dela, 0 para encerra)? '))
    elif a == 0:
        break
print('\n\033[1mPrograma encerrado.\033[m')




