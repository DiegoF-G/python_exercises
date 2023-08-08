from meu_pacote_py import modulo_ex107 as ex107
dinheiro = float(input('Digite um preço: R$ '))
print(f'A metade de {ex107.moeda(dinheiro)} é {ex107.moeda(ex107.metade(dinheiro), "R$")}')
print(f'O dobro de {ex107.moeda(dinheiro)} é {ex107.moeda(ex107.dobro(dinheiro), "R$")}')
print(f'Aumentando 10%, temos {ex107.moeda(ex107.aumentar(dinheiro, 10), "R$")}')
print(f'Reduzindo 15%, temos {ex107.moeda(ex107.diminuir(dinheiro, 15), "R$")}')
