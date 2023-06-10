from meuPacotePy import moduloEx106 as Ex106
dinheiro = float(input('Digite um preço: R$ ').replace(',', '.'))
print(f'A metade de R${dinheiro:.2f} é R${Ex106.metade(dinheiro):.2f}')
print(f'O dobro de R${dinheiro:.2f} é R${Ex106.dobro(dinheiro):.2f}')
print(f'Aumentando 10%, temos R${Ex106.aumentar(dinheiro, 10):.2f}')
print(f'Reduzindo 15%, temos R${Ex106.diminuir(dinheiro, 15):.2f}')


