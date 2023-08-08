s = c = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}º número inteiro: '))
    if n % 2 == 0:
        c += 1
        s += n
print(f'Dos 6 inteiros digitados {c} são pares e a soma deles é {s}')
