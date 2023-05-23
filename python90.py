from random import randint
from time import sleep
print('123456', '\033[1mD6 GAME\033[m', '123456')
resultados = dict()
for i in range(0, 4):
    resultados[f'Jogador {i+1}'] = randint(1, 6)
    print(f'Jogador {i+1} tirou {resultados[f"Jogador {i+1}"]} no D6')
    sleep(1.5)
print(f'Resultado: {resultados}')
print('\033[1mRANKING\033[m')
ranking = sorted(resultados.items(), key=lambda resultado: resultado[1], reverse=True)
r = 1
for k, v in ranking:
    print(f'{r}ªLugar {k}: {v}')
    r += 1
    sleep(1.5)




