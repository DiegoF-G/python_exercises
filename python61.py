print('\033[1mENÉSIMO PRIMEIROS TERMOS DE UMA PA (PROGRESSÃO ARITMÉTICA)\033[m')
a1 = float(input('Primeiro termo: '))
d = float(input('Razão: '))
n = int(input('Número de termos a ser exibido desde o primeiro termo: '))
print(f'Os {n} primeiros termos são: ')
i = -1
while i <= n-2:
    i += 1
    a = a1 + i * d
    if i < n-1:
        print(a, end=' -> ')
    else:
        print(a)

