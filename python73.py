from random import randint
while True:
    rT = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    for i, t in enumerate(rT):
        if i == 0:
            print(f'Os números inteiros positivos sorteados foram: {t}', end=', ')
        elif i < len(rT) - 1:
            print(f'{t}', end=', ')
        else:
            print(f'{t}')
    print(f'O menor e o maior valor sorteados, respectivamente, foram {min(rT)} e {max(rT)}')
    c = input('Deseja sortear novos números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja sortear novos números (S/N)? ').strip()[0]
    if c in 'nN':
        break

# from random import randint
# rT = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# menor = maior = rT[0]
# for i, t in enumerate(rT):
#     if i == 0:
#         print(f'Os números inteiros positivos sorteados foram: {t}', end=', ')
#     elif i < len(rT) - 1:
#        print(f'{t}', end=', ')
#     else:
#        print(f'{t}')
#     if rT[i] > maior:
#         maior = rT[i]
#     elif rT[i] < menor:
#         menor = rT[i]
# print(f'O menor e o maior valor sorteados, respectivamente, foram {menor} e {maior}')







