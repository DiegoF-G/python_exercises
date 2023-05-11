k = int(input('Digite quantos números deseja digitar: '))
num = []
for i in range(0, k):
    num.append(float(input(f'Digite um número: ')))
print(f'A lista dos {k} números digitados é: {num}')
print(f'O maior deles é {max(num)} na(s) posição(ões)', end=' ')
for i, n in enumerate(num):
    if n == max(num):
        print(i, end=' ')
print(f'\nO menor deles é {min(num)} na(s) posição(ões)', end=' ')
for i, n in enumerate(num):
    if n == min(num):
        print(i, end=' ')




