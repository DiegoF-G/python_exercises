"""Nesse arquivo vou explorar alguns métodos dos sets.
   Vale reparar que já usei as funções add, len e set no arquivo python_extra_sets1.py, funcionalidades de sets."""
from meu_pacote_py import cabecalho

acessorios_passat = {'Rodas de Liga', 'Travas Elétricas', 'Piloto Automático', 'Central Multimídia'}
acessorios_crossfox = {'Piloto Automático', 'Teto Panorâmico', '4 X 4', 'Central Multimídia'}
acessorios_jetta = {'Controle de Estabilidade', 'Câmbio Automático', 'Travas Elétricas', 'Rodas de Liga'}

print('Os conjuntos de acessórios do Passat, Crossfox e o Jetta são:')
print(f'\nPassat: {acessorios_passat}\nCrossfox: {acessorios_crossfox}\nJetta: {acessorios_jetta}')
print()

cabecalho('É possível verificar se dois sets possuem ou não elementos em comum', 80)
print(f'O Passat e Crossfox possuem acessórios em comum? {set.isdisjoint(acessorios_passat, acessorios_crossfox)}')
print()

cabecalho('É possível verificar quem são os elementos em comum entre sets', 80)
print(f'O que há em comum entre o Passat e o Jetta? {set.intersection(acessorios_passat, acessorios_jetta)}')
print(f'O que há em comum entre o Crossfox e o Passat? {set.intersection(acessorios_crossfox, acessorios_passat)}')
print(f'O que há em comum entre os três modelos? {set.intersection(acessorios_passat, acessorios_crossfox, acessorios_jetta)}')
print()

cabecalho('É possível juntar elementos de dois ou mais sets em um único set e verificar todos eles', 100)
print('Todos acessórios dos modelos passat, crossfox e jetta:')
acessoriosVW = set.union(acessorios_passat, acessorios_crossfox, acessorios_jetta)
print(acessoriosVW)
print()

"""Repare que se a e b são sets, é válido que: len(set.union(a, b)) == len(a) + len(b) - len(set.intersection(a, b))
de forma análoga, é possível deduzir para união de três ou mais sets"""

cabecalho('É possível verificar se todos elementos de um set também são elementos de outro set "maior"', 100)
acessorios_up = {'Controle de Estabilidade', 'Travas Elétricas', 'Rodas de Liga'}
print(f'Suponha que os acessórios do Up TSI seja: {acessorios_up}')
print(f'Os acessórios do Up TSI também estão no Jetta? {set.issubset(acessorios_up, acessorios_jetta)}')
print()
