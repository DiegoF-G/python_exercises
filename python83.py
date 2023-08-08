nome_peso = list()
pessoas_pesos = list()
pesos = list()
while True:
    nome = input('Nome: ')
    peso = float(input('Peso:'))
    t = (nome_peso.append(nome), nome_peso.append(peso), pessoas_pesos.append(nome_peso[:]), pesos.append(peso),
         nome_peso.clear())
    c = input('Deseja continuar (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar (S/N)? ').strip()[0]
    if c in 'nN':
        break
mais_p = list()
menos_p = list()
for i, peso in enumerate(pesos):
    if peso == max(pesos):
        mais_p.append(pessoas_pesos[i][0])
    if peso == min(pesos):
        menos_p.append(pessoas_pesos[i][0])
print(f'\nAo todo você cadastrou {len(pessoas_pesos)} pessoa(s)')
print(f'O maior peso foi {max(pesos)}kg. Peso de: {mais_p}\nO menor peso foi {min(pesos)}kg. Peso de: {menos_p}')
