x = float(input('Digite um número: '))
maior = menor = x
r = input('Quer continuar (Sim ou Não)? ').strip()[0]
s = 0
c = 1
while r not in 'Nn':
    x = float(input('Digite um número: '))
    s += x
    c += 1
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    r = input('Quer continuar (Sim ou Não)? ').strip()[0]
print(f'Você digitou {c} números, entre eles a média é {s/c} o maior é {maior} e o menor é {menor}.')







