from meuPacotePy import moduloEx108 as Ex108
dinheiro = float(input('Digite um preço: R$ '))
print(f'A metade de {Ex108.moeda(dinheiro)} é {Ex108.metade(dinheiro, monetario=True, unidade="R$")}')
print(f'O dobro de {Ex108.moeda(dinheiro)} é {Ex108.dobro(dinheiro, monetario=True, unidade="R$")}')
print(f'Aumentando 10%, temos {Ex108.aumentar(dinheiro, 10, monetario=True, unidade="R$")}')
print(f'Reduzindo 15%, temos {Ex108.diminuir(dinheiro, 15, monetario=True, unidade="R$")}')
