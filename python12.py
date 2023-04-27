s = float(input('Digite seu salário atual: R$'))
a = float(input('Digite um aumento porcentual (um número maior que 100): '))
print(f'Seu salário com {a}% de aumento ficaria sendo R$ {s*((100 + a)/100):.2f}')
