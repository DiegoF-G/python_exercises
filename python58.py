from math import hypot, pow
print(5*'\033[1:33m=', 'Calculadora', 5*'=', '\033[m')
n1 = float(input('  Digite o primeiro número: '))
n2 = float(input('  Digite o segundo número: '))
o = int(input('''
Opçôes:                 
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
[11] Encerrar execução
Digite a opção desejada com esses números: 
'''))
while o != 11:
    if o == 1:
        print(f'\033[1:33m{n1} + {n2} = {n1 + n2}\033[m')
    elif o == 2:
        print(f'\033[1:33m{n1} - {n2} = {n1 - n2}\033[m')
    elif o == 3:
        print(f'\033[1:33m{n1} . {n2} = {n1 * n2}\033[m')
    elif o == 4:
        print(f'\033[1:33m{n1} / {n2} = {n1 / n2}\033[m')
    elif o == 5:
        print(f'\033[1:33mA média entre {n1} e {n2} é {(n1 + n2) / 2}\033[m')
    elif o == 6:
        print(f'\033[1:33mA parte inteira da divisão de {n1} por {n2} é {n1 // n2}\033[m')
    elif o == 7:
        print(f'\033[1:33mO resto da divisão de {n1} por {n2} é {n1 % n2}\033[m')
    elif o == 8:
        n = int(input('Digite o expoente: '))
        print(f'(\033[1:33m{n1} + {n2})^({n}) = {pow(n1 + n2, n)}\033[m')
    elif o == 9:
        print(f'\033[1:33mA hipotenusa dos números digitados é {hypot(n1, n2)}\033[m')
    elif o == 10:
        n1 = float(input('  Digite o primeiro número: '))
        n2 = float(input('  Digite o segundo número: '))
    elif o >= 12 or o == 0:
        print('\033[0:31mOpção inválida! Tente novamente.\033[m')
    o = int(input('''
Opçôes:                 
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
[11] Encerrar execução
Digite a opção desejada com esses números: 
'''))
print('Calculadora encerrada! Obrigado(a) e volte sempre!')

