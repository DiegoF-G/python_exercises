from meu_pacote_py import modulo_ex108 as ex108
dinheiro = float(input('Digite um preço: R$ '))
print(f'A metade de {ex108.moeda(dinheiro)} é {ex108.metade(dinheiro, monetario=True, unidade="R$")}')
print(f'O dobro de {ex108.moeda(dinheiro)} é {ex108.dobro(dinheiro, monetario=True, unidade="R$")}')
print(f'Aumentando 10%, temos {ex108.aumentar(dinheiro, 10, monetario=True, unidade="R$")}')
print(f'Reduzindo 15%, temos {ex108.diminuir(dinheiro, 15, monetario=True, unidade="R$")}')
