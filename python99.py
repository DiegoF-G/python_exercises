from random import randint


def sortear(n):
    sorteados = list()
    for i in range(0, n):
        sorteados.append(randint(1, 100))
    return sorteados


def soma_par(numeros):
    s = 0
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            s += numeros[i]
    return s


listaNumeros = sortear(int(input('Quantos números você deseja sortear, cada um entre 1 a 100? ')))
print(f'\nOs {len(listaNumeros)} números sorteados foram: {str(listaNumeros).replace("[", "").replace("]", "")}')
print(f'A soma de todos os pares foi {soma_par(listaNumeros)}.')

