from random import randint
from time import sleep
print('\033[1:mPAR OU ÍMPAR\033[m')
c = 0
while True:
    n_jogador = int(input('Digite um valor inteiro de 1 a 10: '))
    while n_jogador > 10 or n_jogador < 1:
        n_jogador = int(input('Número inválido! Digite novamente um valor inteiro de 1 a 10: '))
    a_jogador = input('Par ou Ímpar? ').strip()[0]
    while a_jogador not in 'pPiIíÍ':
        a_jogador = input('Aposta inválida! Par ou Ímpar? ').strip()[0]
    npc = randint(1, 10)
    soma = n_jogador + npc
    sleep(1.5)
    if soma % 2 == 0 and a_jogador in 'pP':
        c += 1
        print(f'Parabéns! Você jogou {n_jogador} e eu {npc} e assim a soma deu {soma} que é par, portanto você ganhou!')
        print('Vamos jogar mais uma vez...\n ')
    elif soma % 2 != 0 and a_jogador in 'pP':
        print(f'Você perdeu! Você jogou {n_jogador} e eu {npc} e assim a soma deu {soma} que é ímpar.')
        break
    elif soma % 2 == 0 and a_jogador in 'iIíÍ':
        print(f'Você perdeu! Você jogou {n_jogador} e eu {npc} e assim a soma deu {soma} que é par.')
        break
    elif soma % 2 != 0 and a_jogador in 'iIíÍ':
        c += 1
        print(f'Parabéns! Você jogou {n_jogador} e eu {npc} e assim a soma deu {soma} que é ímpar, portanto você ganhou!')
        print('Vamos jogar mais uma vez...\n ')
print(f'\033[1:35mGAME OVER!\033[m Você conseguiu {c} vitória(s) consecutiva(s).')
