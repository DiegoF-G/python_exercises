nomePeso = list()
pessoasPesos = list()
pesos = list()
while True:
    nome = input('Nome: ')
    peso = float(input('Peso:'))
    t = (nomePeso.append(nome), nomePeso.append(peso), pessoasPesos.append(nomePeso[:]), pesos.append(peso),
         nomePeso.clear())
    c = input('Deseja continuar (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar (S/N)? ').strip()[0]
    if c in 'nN':
        break
maisP = list()
menosP = list()
for i, peso in enumerate(pesos):
    if peso == max(pesos):
        maisP.append(pessoasPesos[i][0])
    if peso == min(pesos):
        menosP.append(pessoasPesos[i][0])
print(f'\nAo todo você cadastrou {len(pessoasPesos)} pessoa(s)')
print(f'O maior peso foi {max(pesos)}kg. Peso de: {maisP}\nO menor peso foi {min(pesos)}kg. Peso de: {menosP}')





