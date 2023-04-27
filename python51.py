print('\033[1mIdentificador de Primos\033[m')
n = int(input('Digite um número inteiro positivo: '))
c = 0
for i in range(1, n + 1):
    if n % i == 0 and i != n:
        c += 1
        print(f'\033[1:31m{i}\033[m', end=' ')
    elif n % i == 0:
        c += 1
        print(f'\033[1:31m{i}\033[m')
    else:
        print(f'\033[0:33m{i}\033[m', end=' ')
if c == 2:
    print(f'{n} é \033[1mprimo\033[m!')
else:
    print(f'{n} é um \033[1mnúmero composto\033[m.')


