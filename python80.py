from math import sqrt
num = []
psq = []
sqr = []
while True:
    x = float(input('Digite um número: '))
    if sqrt(x) - int(sqrt(x)) == 0:
        psq.append(x)
        sqr.append(sqrt(x))
    num.append(x)
    c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    if c in 'nN':
        break
num.sort(reverse=True)
psq.sort(reverse=True)
sqr.sort(reverse=True)
t = (print(f'\nVocê digitou {len(num)} número(s).'), print(f'Lista resultante dos números em ordem descrescente: {num}'))
if len(sqr) > 0:
    print(f'Lista dos quadrados perfeitos que foram encontrados em ordem descrescente: {psq}')
    print(f'Lista das raízes quadradas dos quadrados perfeitos em ordem descrescente: {sqr}')
else:
    print('Nenhum quadrado perfeito foi encontrado na lista.')
print('O número da besta foi encontrado na lista!' if 666 in num else 'O número da besta não foi encontrado na lista.')



