num = []
while True:
    x = float(input('Digite um número: '))
    num.append(x)
    c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    if c in 'nN':
        break
num.sort(reverse=True)
t = (print(f'Você digitou {len(num)} número(s).'), print(f'Lista resultante dos números em ordem descrescente: {num}'))
print('O número 5 foi encontrado na lista!' if 5 in num else 'O número 5 não foi encontrado na lista.')


