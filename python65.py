s = c = 0
while True:
    f = float(input('Digite um número (999 para parar): '))
    if f == 999:
        print(f'Você digitou {c} números cuja soma total é {s}')
        break
    s += f
    c += 1
