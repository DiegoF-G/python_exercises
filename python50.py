print('\033[1m10 PRIMEIROS TERMOS DE UMA PA (PROGRESSÃO ARITMÉTICA)\033[m')
a1 = int(input('Primeiro termo: '))
d = float(input('Razão: '))
print(f'Os 10 primeiros termos são: ')
for i in range(0, 10):
    a = a1 + i * d
    if i < 9:
        print(a, end=' -> ')
    else:
        print(a)





