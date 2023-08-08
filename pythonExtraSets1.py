"""Set é uma coleção de dados não ordenada que possui todos os seus elementos distintos dois a dois.
   Vale observar que os sets são totalmente análogos aos conjuntos na Matemática, uma versão "Python" deles.
   Nesse arquivo explorei algumas das suas características."""
from meu_pacote_py import cabecalho

listaCarros = ['Jetta Variant', 'Passat', 'Crossfox', 'Dodge Jorney', 'Passat']
setCarros = set(listaCarros)
cabecalho('Temos a seguinte lista e set, respectivamente:', 50)
listaSet = (print(listaCarros), print(setCarros))

cabecalho('Sets não possuem elementos repetidos e caso tenha eles são "unificados"', 75)
print(f'Quantidade de elementos na lista de carros: {len(listaCarros)}')
print(f'Quantidade de elementos no conjunto (set) de carros: {len(setCarros)}')

cabecalho('Sets podem possuir dados de diferentes tipos e são mutáveis', 65)
onix = {2017, "Onix", 37123.04, True}
print(onix)
onix.add('1.0 turbo')
print(onix)

cabecalho('É possível realizar uma especificação em um objeto set, para o "frozenset", que são sets imutáveis', 105)
onix = frozenset(onix)
try:
    onix.add('1.0 aspirado')
except AttributeError:
    print('\033[0:31mFrozensets são imutáveis! Não é possível modifica-los!\033[m')

cabecalho('Sets não são enumeráveis (não são indexados), diferente do que pode ser um conjunto na Matemática', 105)
raise TypeError('Ops! Não sei onde é o endereço 0 pois isso é um set!')
print(setCarros[0])
