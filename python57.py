from random import randint
from time import sleep
n = randint(1, 10)
print('-==-'*20)
print('\033[1:35mVou pensar em um número inteiro de 1 a 10. Tente advinhar ele em 5 tentativas...\033[m')
print('-==-'*20)
sleep(1)
print('\033[1:35mEstou pensando...\033[m')
sleep(2)
un = int(input('Digite um inteiro de 1 a 10: '))
while un < 1 or un > 10:
    un = int(input('\033[1:31mNúmero inválido!\033[m \nDigite novamente um número inteiro, de 1 a 10: '))
t = 1
while not (un == n or t == 5):
    if 0 < un < n:
        t += 1
        print('\033[1:35mO número que pensei não é esse, é maior...\033[m')
        sleep(0.7)
        un = int(input('Digite novamente um inteiro de 1 a 10: '))
    elif 11 > un > n:
        t += 1
        print('\033[1:35mO número que pensei não é esse, é menor...\033[m')
        sleep(0.7)
        un = int(input('Digite novamente um inteiro de 1 a 10: '))
    else:
        un = int(input('\033[1:31mNúmero inválido!\033[m \nDigite novamente um número inteiro, de 1 a 10: '))
sleep(1)
if t == 1:
    print('\033[1:35mParabéns, você acertou com uma única tentativa!!! Seu paranormal!\033[m')
elif 1 < t <= 3:
    print(f'\033[1:35mParabéns! Você acertou com apenas {t} tentativas!\033[m')
elif 3 < t <= 5 and un == n:
    print(f'\033[1:35mVocê acertou! Com {t} tentativas.\033[m')
else:
    print(f'\033[1:35mVocê perdeu! O número pensado por mim era {n}.\033[m')

# Qual a melhor estratégia para vencer esse jogo? Eu gosto sempre de apostar no 5 hehe







