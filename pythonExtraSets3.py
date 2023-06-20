# O desempenho para pesquisar elementos em variáveis compostas (estruturas de dados) varia para cada tipo...
from time import time
elementosSet = set(range(10000))
elementosList = list(range(10000))
elementosTuple = tuple(range(10000))


def verificar_elemento_in(elemento_iteravel):
    for i in range(10000):
        if i in elemento_iteravel:
            pass


i1 = time()
verificar_elemento_in(elementosTuple)
f1 = time()
print(f'Tempo de execução tuplas: {f1 - i1}')
i2 = time()
verificar_elemento_in(elementosList)
f2 = time()
print(f'Tempo de execução lista: {f2 - i2}')
i3 = time()
verificar_elemento_in(elementosSet)
f3 = time()
print(f'Tempo de execução set: {f3 - i3}')

# Conclusão: sets são mais rápidos para pesquisar seus elementos
