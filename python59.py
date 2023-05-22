print('\033[1:33mFATORIAL\033[m')
n = int(input('Digite um inteiro não-negativo: '))
while not n >= 0:
    n = int(input('Número inválido! Digite novamente um inteiro não-negativo: '))
n1 = n
if n > 0:
    for i in range(1, n):
        n *= i
    print(f'{n1}! = {n}')
else:
    print('0! = 1')
# Outra solução:
# n = int(input('Digite um inteiro não-negativo: '))
# while not n >= 0:
#     n = int(input('Número inválido! Digite novamente um inteiro não-negativo: '))
# n1 = n
# n2 = n
# if n > 0:
#     while n1 > 1:
#         n1 -= 1
#         n2 *= n1
#     print(f'{n}! = {n2}')
# else:
#     print('0! = 1')
# Outra solução também:
# from math import factorial
# n = int(input('Digite um inteiro não-negativo: '))
# f = factorial(n)
# printO(f'`{n}! = f')










