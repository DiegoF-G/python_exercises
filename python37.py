n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 < n2:
    print(f'O segundo valor é \033[1mmaior\033[m que o primeiro')
elif n1 > n2:
    print(f'O primeiro valor é \033[1mmaior\033[m que o segundo')
else:
    print(f'O primerio e segundo são \033[1miguais\033[m')
