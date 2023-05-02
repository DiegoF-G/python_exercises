while True:
    print('~'*40)
    n = float(input(f'Deseja ver a tabuada de qual número (digite um negativo para encerrar)? '))
    if n < 0:
        break
    print('~'*40)
    for i in range(1, 11):
        print(f'{n} . {i} = {n*i}')
print('Tabuada encerrada.')

