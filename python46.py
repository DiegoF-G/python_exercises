print('\033[1mLISTA DE NÚMEROS PARES\033[m')
n = int(input('Digite um inteiro não negativo: '))
print(f'Todos os pares de 0 até {n} são: ')
for i in range(0, n+1, 2):
    print(i, end=' ')
