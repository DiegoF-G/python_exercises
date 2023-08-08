from bisect import insort
num = [[], []]
for i in range(0, 10):
    n = int(input(f'Digite o {i+1}ª número inteiro: '))
    if n % 2 == 0:
        insort(num[0], n)
    else:
        insort(num[1], n)
t = (print(f'\nOs números pares digitados foram: {num[0]}'), print(f'Os números ímpares digitados foram: {num[1]}'))
