from random import randint
from time import sleep
ms = (print('\033[1:33m-'*60), print(f'{"MEGA SENA":^60}'), print('-'*59 + '-\033[m'))
n_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
for i in range(0, n_jogos):
    jogos.append([])
print('-='*6, f'Sorteando {n_jogos} jogos', '=-'*6)
for i in range(0, n_jogos):
    sleep(1.5)
    j = 0
    while j <= 5:
        j += 1
        n = randint(1, 60)
        if n not in jogos[i]:
            jogos[i].append(n)
        else:
            j -= 1
    print(f'Jogo {i+1}: {jogos[i]}')
sleep(1)
print('\033[1mBOA SORTE!!!\033[m')
