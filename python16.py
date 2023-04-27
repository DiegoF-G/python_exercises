# from math import sqrt, pow
# b = float(input('Digite o comprimento do cateto: '))
# c = float(input('Digite o comprimento do outro cateto: '))
# print(f'A hipotenusa desse triangulo retangulo com os catetos informados tem medida de', end=' ')
# print(sqrt(pow(b, 2) + pow(c, 2)))
from math import hypot
b = float(input('Digite o comprimento do cateto: '))
c = float(input('Digite o comprimento do outro cateto: '))
print(f'A hipotenusa desse triangulo retângulo com os catetos informados mede aproximadamente', end=' ')
print(f'{hypot(b,c):.2f}')






