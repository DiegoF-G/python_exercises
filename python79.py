# Não posso usar o método sort() e nem módulo. Solução apenas com python e outra com módulo padrão do python, respectiv.
k = int(input('Quantos números você deseja adicionar na lista? '))
num = []
for i in range(0, k):
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

# from bisect import insort
# k = int(input('Quantos números você deseja adicionar na lista? '))
# num = []
# for i in range(0, k):
#     n = float(input('Digite um número: '))
#     insort(num, n)
#     print(f'Número adicionado na posição {num.index(n)}...')
# print(f'Lista resultante dos números em ordem crescente: {num}')
















