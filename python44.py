from time import sleep
from random import randint
import emoji

print('-=-'*5, '\033[1:33mJOKENPO\033[m', '-=-'*5)

print('Escolha entre:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
itens = 'PEDRA PAPEL TESOURA'.split()
ej = int(input('Qual a sua escolha? '))
ec = randint(0, 2)

sleep(0.5)
print('\033[33mJO...\033[m')
sleep(0.8)
print('\033[33mKEN...\033[m')
sleep(1)
print('\033[33mPO!!!\033[m')

print('=-='*8)
print(f'Eu escolhi {itens[ec]}')
print(f'Você escolheu {itens[ej]}')
print('=-='*8)

if ej == 0:
    if ec == 0:
        print('EMPATE!')
    elif ec == 1:
        print('Você PERDEU!', emoji.emojize('😨'))
    elif ec == 2:
        print('Você GANHOU!', emoji.emojize('🤩'))
elif ej == 1:
    if ec == 0:
        print('Você GANHOU!', emoji.emojize('🤩'))
    elif ec == 1:
        print('EMPATE!')
    elif ec == 2:
        print('Você PERDEU!', emoji.emojize('😨'))
elif ej == 2:
    if ec == 0:
        print('Você PERDEU!', emoji.emojize('😨'))
    elif ec == 1:
        print('Você GANHOU!', emoji.emojize('🤩'))
    elif ec == 2:
        print('EMPATE!')






