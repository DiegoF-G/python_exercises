from random import randint
from time import sleep
print('\033[1:mPAR OU ÍMPAR\033[m')
c = 0
while True:
    nJogador = int(input('Digite um valor inteiro de 1 a 10: '))
    while nJogador > 10 or nJogador < 1:
        nJogador = int(input('Número inválido! Digite novamente um valor inteiro de 1 a 10: '))
    aJogador = input('Par ou Ímpar? ').strip()[0]
    while aJogador not in 'pPiIíÍ':
        aJogador = input('Aposta inválida! Par ou Ímpar? ').strip()[0]
    nPc = randint(1, 10)
    soma = nJogador + nPc
    sleep(1.5)
    if soma % 2 == 0 and aJogador in 'pP':
        c += 1
        print(f'Parabéns! Você jogou {nJogador} e eu {nPc} e assim a soma deu {soma} que é par, portanto você ganhou!')
        print('Vamos jogar mais uma vez...\n ')
    elif soma % 2 != 0 and aJogador in 'pP':
        print(f'Você perdeu! Você jogou {nJogador} e eu {nPc} e assim a soma deu {soma} que é ímpar.')
        break
    elif soma % 2 == 0 and aJogador in 'iIíÍ':
        print(f'Você perdeu! Você jogou {nJogador} e eu {nPc} e assim a soma deu {soma} que é par.')
        break
    elif soma % 2 != 0 and aJogador in 'iIíÍ':
        c += 1
        print(f'Parabéns! Você jogou {nJogador} e eu {nPc} e assim a soma deu {soma} que é ímpar, portanto você ganhou!')
        print('Vamos jogar mais uma vez...\n ')
print(f'\033[1:35mGAME OVER!\033[m Você conseguiu {c} vitória(s) consecutiva(s).')














