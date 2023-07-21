# Set é uma coleção de dados (também uma classe) não-ordenada e que possui todos seus elementos distintos dois a dois.
# Vale observar que os sets são totalmente análogos aos conjuntos na Matemática, uma versão "Python" deles.
# Nesse arquivo explorei algumas de suas características.

from meuPacotePy import cabecalho
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

cabecalho('Sets não são enumeráveis (não são indexados), diferente do que pode ser um conjunto na Matemática', 105)
try:
    print(setCarros[0])
finally:
    raise TypeError('Ops! Não sei onde é o endereço 0 pois isso é um set!')
