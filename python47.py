print('\033[1mSOMA DE TODOS ÍMPARES MÚLTIPLOS DE 3\033[m')
n = int(input('Digite um inteiro não negativo: '))
s = 0
c = 0
for i in range(0, n + 1):
    if i % 2 != 0 and i % 3 == 0:
        c += 1
        s += i
print(f'A soma dos {c} números ímpares e múltiplos de 3 de 0 a {n} é: {s}')
