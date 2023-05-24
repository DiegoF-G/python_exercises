from random import randint
from time import sleep
print('123456', '\033[1mD6 GAME\033[m', '123456')
sleep(1)
resultados = dict()
for i in range(0, 4):
    resultados[f'Jogador {i+1}'] = randint(1, 6)
    print(f'Jogador {i+1} tirou {resultados[f"Jogador {i+1}"]} no D6')
    sleep(1.5)
print(f'\nResultado: {resultados}')
sleep(1)
print('\n\033[1mRANKING\033[m')
sleep(1)
ranking = sorted(resultados.items(), key=lambda resultado: resultado[1], reverse=True)
r = 1
for k, v in ranking:
    if v == ranking[r-2][1] and r > 1:
        r -= 1
    print(f'{r}ªLugar {k}: {v}')
    r += 1
    sleep(1)





