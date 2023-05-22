print('\033[7mMaior de 3\033[m')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'{maior} é o maior dos números digitados')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'{menor} é o menor dos números digitados')
# if n1 > n2 > n3:
#    print(f'{n1} é o maior dos números digitados')
#    print(f'{n3} é o menor dos números digitados')
# if n1 > n3 > n2:
#     print(f'{n1} é o maior dos números digitados')
#     print(f'{n2} é o menor dos números digitados')
# if n2 > n3 > n1:
#     print(f'{n2} é o maior dos números digitados')
#     print(f'{n1} é o menor dos números digitados')
# if n2 > n1 > n3:
#     print(f'{n2} é o maior dos números digitados')
#     print(f'{n3} é o menor dos números digitados')
# if n3 > n2 > n1:
#     print(f'{n3} é o maior dos números digitados')
#     print(f'{n1} é o menor dos números digitados')
# if n3 > n1 > n2:
#     print(f'{n3} é o maior dos números digitados')
#     print(f'{n2} é o menor dos números digitados')


