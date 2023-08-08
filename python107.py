from meuPacotePy import moduloEx107 as Ex107
dinheiro = float(input('Digite um preço: R$ '))
print(f'A metade de {Ex107.moeda(dinheiro)} é {Ex107.moeda(Ex107.metade(dinheiro), "R$")}')
print(f'O dobro de {Ex107.moeda(dinheiro)} é {Ex107.moeda(Ex107.dobro(dinheiro), "R$")}')
print(f'Aumentando 10%, temos {Ex107.moeda(Ex107.aumentar(dinheiro, 10), "R$")}')
print(f'Reduzindo 15%, temos {Ex107.moeda(Ex107.diminuir(dinheiro, 15), "R$")}')
