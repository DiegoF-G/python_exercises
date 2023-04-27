s = float(input('Qual o salário do funcionário? R$ '))
if s <= 1250:
    sa = s*1.15
else:
    sa = s*1.10
print(f'Quem ganhava R${s} passa a ganhar R${sa:.2f} agora')


