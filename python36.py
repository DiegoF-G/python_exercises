print('\033[1:34mConversor de Base Númerica\033[m')
n = int(input('Digite um número inteiro: '))
print('Digite a opção para converter o inteiro decimal digitado para:\n1-binário\n2-hexadecimal\n3-octal')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} = {bin(n)[2:]} em binário')
elif o == 2:
    print(f'{n} = {hex(n)[2:]} em hexadecimal')
elif o == 3:
    print(f'{n} = {oct(n)[2:]} em octal')
else:
    print('\033[1:31mOpção digitada inválida. Tente novamente.\033[m')
