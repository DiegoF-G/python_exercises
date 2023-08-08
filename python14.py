dias_alugado = int(input('Quantos dias você permaneceu com o carro? '))
quanto_rodou = float(input('Quantos quilometros rodou? '))
print(f'Com {dias_alugado} dia(s) de uso e {quanto_rodou:.1f} km rodado(s) o total a pagar fica por:', end=' ')
print('R$', dias_alugado*60 + quanto_rodou*0.15)

# R$60,00 por dia e R$0,15 por km
