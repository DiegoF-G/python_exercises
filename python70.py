print('='*15, '\033[1:33mPY BANK\033[m', '='*15)
x = int(input(' Valor do saque: R$ '))
while x == 0:
    r = input('Deseja sair do saque (S/N)? ').strip().upper()[0]
    while r not in 'sSnN':
        r = input('Deseja sair do saque (S/N)? ').strip().upper()[0]
    if r == 'S':
        break
    x = int(input(' Digite novamente o valor do saque: R$ '))
i = j = k = m = n = 0
while True:
    if x >= 50:
        i = x // 50
        x -= i*50
    if 20 <= x < 50:
        j = x // 20
        x -= j*20
    if 10 <= x < 20:
        k = x // 10
        x -= k*10
    if 5 <= x < 10:
        m = x // 5
        x -= m*5
    if x < 5:
        n = x
        break
print('-'*37)
if i > 0:
    print(f'Total de {i} cédulas de R$50,00')
if j > 0:
    print(f'Total de {j} cédulas de R$20,00')
if k > 0:
    print(f'Total de {k} cédulas de R$10,00')
if m > 0:
    print(f'Total de {m} cédulas de R$5,00')
if n > 0:
    print(f'Total de {n} cédulas de R$1,00')
print('\033[0:36mPY BANK agradece, volte sempre!\033[m')
# R$50, R$20, R$10 e R$1 são as notas nesse caixa eletrônico



