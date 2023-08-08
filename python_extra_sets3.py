# O desempenho para pesquisar elementos em variáveis compostas (estruturas de dados) varia para cada tipo...
from time import time

elementos_set = set(range(10000))
elementos_list = list(range(10000))
elementos_tuple = tuple(range(10000))


def verificar_elemento_in(elemento_iteravel):
    for i in range(10000):
        if i in elemento_iteravel:
            pass


i1 = time()
verificar_elemento_in(elementos_tuple)
f1 = time()
print(f'Tempo de execução tuplas: {f1 - i1}')
i2 = time()
verificar_elemento_in(elementos_list)
f2 = time()
print(f'Tempo de execução lista: {f2 - i2}')
i3 = time()
verificar_elemento_in(elementos_set)
f3 = time()
print(f'Tempo de execução set: {f3 - i3}')

# Conclusão: sets são mais rápidos para pesquisar seus elementos
