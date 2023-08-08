from random import randint
from time import sleep
n = randint(1, 5)
print('-==-'*15)
print('\033[1:35mVou pensar em um inteiro de 1 a 5. Tente advinhar...\033[m')
print('-==-'*15)
sleep(1)
print('Estou pensando...')
sleep(2)
nu = int(input('Digite um inteiro de 1 a 5: '))
if nu == n:
    print(f'{n} é o número que eu pensei! Parabens, seu Alakazam!')
else:
    print(f'Que azar, errou! O número que eu pensei era {n}')
