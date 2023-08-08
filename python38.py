from datetime import date
print('\033[4:32mAlistamento Militar\033[m')
b = int(input('Qual seu ano de nascimento: '))
y = date.today().year - b
ano_alistamento = date.today().year + (18-y)
if y < 18:
    print(f'''Ainda faltam cerca de {18-y} anos para seu alistamento.
Seu alistamento será em {ano_alistamento}''')
elif y > 18:
    print(f'''Você já deveria ter se alistado há cerca de {y-18} anos.
Seu alistamento foi em {ano_alistamento}''')
else:
    print(f'Seu alistamento é nesse ano!')
