n1 = float(input('Nota na primeira prova: '))
n2 = float(input('Nota na segunda prova: '))
m = (n1 + n2)/2
if m >= 7:
    print(f'Parabéns! Sua média foi {m:.1f} e você foi aprovado!' )
elif 5 <= m < 7:
    print(f'Sua média foi {m:.1f} e você está de exame final, boa prova!')
else:
    print(f'Infelizmente você foi \033[1:31mreprovado\033[m, sua média foi {m:.1f}.')

