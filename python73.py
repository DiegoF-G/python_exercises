from random import randint
while True:
    r = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    for i, t in enumerate(r):
        if i == 0:
            print(f'Os números inteiros positivos sorteados foram: {t}', end=', ')
        elif i < len(r) - 1:
            print(f'{t}', end=', ')
        else:
            print(f'{t}')
    print(f'O menor e o maior valor sorteados, respectivamente, foram {min(r)} e {max(r)}')
    c = input('Deseja sortear novos números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja sortear novos números (S/N)? ').strip()[0]
    if c in 'nN':
        break

# from random import randint
# r = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# menor = maior = r[0]
# for i, t in enumerate(r):
#     if i == 0:
#         print(f'Os números inteiros positivos sorteados foram: {t}', end=', ')
#     elif i < len(r) - 1:
#        print(f'{t}', end=', ')
#     else:
#        print(f'{t}')
#     if r[i] > maior:
#         maior = r[i]
#     elif r[i] < menor:
#         menor = r[i]
# print(f'O menor e o maior valor sorteados, respectivamente, foram {menor} e {maior}')
