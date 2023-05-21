diasAlugado = int(input('Quantos dias você permaneceu com o carro? '))
quantoRodou = float(input('Quantos quilometros rodou? '))
print(f'Com {diasAlugado} dias de uso e {quantoRodou:.1f} km rodados o total a pagar fica por:', end=' ')
print('R$', diasAlugado*60 + quantoRodou*0.15)
# R$60,00 por dia e R$0,15 por km
