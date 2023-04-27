v = float(input('Valor total das compras: R$'))
print('''OPÇÕES DE PAGAMENTO:
[1] À vista no dinheiro ou cheque, com 10% de desconto
[2] À vista no cartão, com 5% de desconto
[3] 2x no cartão sem juros
[4] 3x ou mais vezes, com juros''')
f = int(input('Digite a opção de pagamento: '))
if f == 1:
    print(f'O total a pagar fica por R${v*0.9:.2f}')
elif f == 2:
    print(f'O total que será cobrado no cartão será R${v*0.95:.2f}')
elif f == 3:
    print(f'O valor, em 2 vezes, da parcela ficará por R${v/2:.2f}')
elif f == 4:
    p = int(input('Em quantas vezes deseja parcelar? '))
    print(f'O valor, em {p} vezes, da parcela ficará por R${(v/p)*1.15:.2f}')
else:
    print('\033[0:31mOpção inválida\033[m, digite novamente o número referente a opção desejada')
