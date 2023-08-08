from bisect import insort
num = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    if c in 'nN':
        break
par = []
impar = []
for n in num:
    if n % 2 == 0:
        insort(par, n)
    else:
        insort(impar, n)
t = (print(f'\nLista resultante dos inteiros digitados: {num}'), print(f'Lista dos pares digitados: {par}'),
     print(f'Lista dos ímpares digitados: {impar}'))
