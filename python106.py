from meu_pacote_py import modulo_ex106 as ex106
dinheiro = float(input('Digite um preço: R$ ').replace(',', '.'))
print(f'A metade de R${dinheiro:.2f} é R${ex106.metade(dinheiro):.2f}')
print(f'O dobro de R${dinheiro:.2f} é R${ex106.dobro(dinheiro):.2f}')
print(f'Aumentando 10%, temos R${ex106.aumentar(dinheiro, 10):.2f}')
print(f'Reduzindo 15%, temos R${ex106.diminuir(dinheiro, 15):.2f}')
