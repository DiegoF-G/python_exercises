k = int(input('Digite quantos números deseja digitar: '))
num = []
for i in range(1, k+1):
    num.append(float(input(f'Digite um número: ')))
print(f'A lista dos {k} números digitados é: {num}')
for i, n in enumerate(num):
    if i == num.index(max(num)):
        print(f'O maior deles é {n} na(s) posição(ões) {i}', end=' ')
    elif n == max(num) and i > num.index(max(num)):
        print(i, end=' ')
for i, n in enumerate(num):
    if i == num.index(min(num)):
        print(f'\nO menor deles é {n} na(s) posição(ões) {i}', end=' ')
    elif n == min(num) and i > num.index(min(num)):
        print(i, end=' ')



