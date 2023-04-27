from math import hypot, pow
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
o = int(input('''Digite a opção desejada com esses números: 
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Média simples
    [6] Divisão inteira
    [7] Resto da divisão
    [8] Potência da soma
    [9] Hipotenusa
    [10] Digitar novos números
    [11] Encerrar execução'''))
o = 0
while o != 11:
    if o == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif o == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif o == 3:
        print(f'{n1} . {n2} = {n1 * n2}')
    elif o == 4:
        print(f'{n1} / {n2} = {n1 / n2}')
    elif o == 5:
        print(f'A média entre {n1} e {n2} é {(n1 + n2) / 2}')
    elif o == 6:
        print(f'A parte inteira da divisão de {n1} por {n2} é {n1 // n2}')
    elif o == 7:
        print(f'O resto da divisão de {n1} por {n2} é {n1 % n2}')
    elif o == 8:
        n = int(input('Digite o expoente: '))
        print(f'({n1} + {n2})^({n}) = {pow(n1 + n2, n)}')
    elif o == 9:
        print(f'A hipotenusa dos números digitados é {hypot(n1, n2)}')
    elif o == 10:
        n1 = float(input(f'{}'))

