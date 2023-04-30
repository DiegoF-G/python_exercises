s = c = 0
f = float(input('Digite um número (999 para parar): '))
while not f == 999:
    c += 1
    s += f
    f = float(input('Digite um número (999 para parar): '))
print(f'A soma dos {c} números digitados é {s}.')



