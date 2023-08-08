print('\033[1m10 PRIMEIROS TERMOS DE UMA PA (PROGRESSÃO ARITMÉTICA)\033[m')
a1 = float(input('Primeiro termo: '))
d = float(input('Razão: '))
print('Os 10 primeiros termos são: ')
i = -1
while i <= 8:
    i += 1
    a = a1 + i * d
    if i < 9:
        print(a, end=' -> ')
    else:
        print(a)
