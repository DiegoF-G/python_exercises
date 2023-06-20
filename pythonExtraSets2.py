# Nesse arquivo vou explorar alguns métodos dos sets
# Vale reparar que já usei o método add e as funções len e set no arquivo pythonExtraSets1.py, funcionalidades de sets
from meuPacotePy import cabecalho
acessoriosPassat = {'Rodas de Liga', 'Travas Elétricas', 'Piloto Automático', 'Central Multimídia'}
acessoriosCrossfox = {'Piloto Automático', 'Teto Panorâmico', '4 X 4', 'Central Multimídia'}
acessoriosJetta = {'Controle de Estabilidade', 'Câmbio Automático', 'Travas Elétricas', 'Rodas de Liga'}
print('Os conjuntos de acessórios do Passat, Crossfox e o Jetta são:')
print(f'Passat: {acessoriosPassat}\nCrossfox: {acessoriosCrossfox}\nJetta: {acessoriosJetta}')
print()

cabecalho('É possível verificar se dois sets possuem ou não elementos em comum', 80)
print(f'O Passat e Crossfox possuem acessórios em comum? {set.isdisjoint(acessoriosPassat, acessoriosCrossfox)}')
print()

cabecalho('É possível verificar quem são os elementos em comum entre sets', 80)
print(f'O que há em comum entre o Passat e o Jetta? {set.intersection(acessoriosPassat, acessoriosJetta)}')
print(f'O que há em comum entre o Crossfox e o Passat? {set.intersection(acessoriosCrossfox, acessoriosPassat)}')
print(f'O que há em comum entre os três modelos? {set.intersection(acessoriosPassat, acessoriosCrossfox, acessoriosJetta)}')
print()

cabecalho('É possível juntar elementos de dois ou mais sets em um único set e verificar todos eles', 90)
print('Todos acessórios dos modelos passat, crossfox e jetta:')
acessoriosVW = set.union(acessoriosPassat, acessoriosCrossfox, acessoriosJetta)
print(acessoriosVW)
print()

# repare que se a e b são sets, é válido que: len(set.union(a, b)) == len(a) + len(b) - len(set.intersection(a, b))
# de forma análoga é possível deduzir para união de três ou mais sets

cabecalho('É possível verificar se todos elementos de um set também são elementos de outro', 90)
acessoriosUp = {'Controle de Estabilidade', 'Travas Elétricas', 'Rodas de Liga'}
print(f'Suponha que os acessórios do Up TSI seja: {acessoriosUp}')
print(f'Os acessórios do Up também estão no Jetta? {set.issubset(acessoriosUp, acessoriosJetta)}')


