print('='*16)
print(' \033[1mBARATÃO STORE\033[m')
print('='*16)
s = caro = 0
produtoBarato = ''
name = input('Nome do produto: ')
price = float(input('Preço do produto: R$ '))
barato = price
while True:
    s += price
    if price < barato:
        barato = price
        produtoBarato = name
    if price > 1000:
        caro += 1
    c = input('Continuar comprando (S/N)? ').strip().upper()[0]
    print(' ')
    while c not in 'SN':
        c = input('Continuar comprando (S/N)? ').strip().upper()[0]
        print(' ')
    if c == 'N':
        break
    name = input('Nome do produto: ')
    price = float(input('Preço do produto: R$ '))
print('-'*20)
print(f'O valor total da compra foi de R${s}')
print(f'Temos {caro} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoBarato} custando R${barato}')

# print('='*16)
# print(' \033[1mBARATÃO STORE\033[m')
# print('='*16)
# s = caro = barato = i = 0
# produtoBarato = ''
# while True:
#     i += 1
#     name = input('Nome do produto: ')
#     price = float(input('Preço do produto: R$ '))
#     c = input('Continuar comprando (S/N)? ').strip().upper()[0]
#     print(' ')
#     while c not in 'SN':
#         c = input('Continuar comprando (S/N)? ').strip().upper()[0]
#         print(' ')
#     s += price
#     if i == 1 or price < barato:
#         barato = price
#         produtoBarato = name
#     if price > 1000:
#         caro += 1
#     if c == 'N':
#         break
# print('-'*20)
# print(f'O valor total da compra foi de R${s}')
# print(f'Temos {caro} produto(s) custando mais de R$1000.00')
# print(f'O produto mais barato foi {produtoBarato} custando R${barato}')







