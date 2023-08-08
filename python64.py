x = float(input('Digite um número: '))
maior = menor = s = x
c = 1
r = input('Quer continuar (Sim ou Não)? ').strip()[0]
while r not in 'Nn':
    x = float(input('Digite um número: '))
    s += x
    c += 1
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    r = input('Quer continuar (Sim ou Não)? ').strip()[0]
print(f'Você digitou {c} números. Entre eles a média é {s/c}, o maior é {maior} e o menor é {menor}.')
