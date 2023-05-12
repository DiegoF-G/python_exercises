# Não posso usar o método sort()
num = []
for i in range(0, 5):
    n = float(input('Digite um número: '))
    if i == 0:
        num.append(n)
        print('Esse número será adicionado na posição 0...')
    elif n > num[-1]:
        num.append(n)
        print(f'Esse número será adicionado na posição {len(num) - 1}...')
    else:
        j = 0
        while j < len(num):
            if n <= num[j]:
                num.insert(j, n)
                print(f'Esse número será adicionado na posição {j}...')
                break
            else:
                j += 1
print(f'Lista resultante dos números em ordem crescente: {num}')
















