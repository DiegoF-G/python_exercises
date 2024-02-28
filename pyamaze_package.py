from pyamaze import maze


# Encapsulando os comandos para criar o labirinto
def labirinto(l=5, c=5, xf=5, yf=5, show=False, paths_percent=0):
    lab = maze(l, c)
    lab.CreateMaze(xf, yf, loopPercent=paths_percent)
    if show:
        lab.run()
    return lab


# Chamando a função "labirinto"
labirinto(show=True)

# Células do labirinto, indicando suas coordenadas
celulas = labirinto().grid
print(f'Células: {celulas}\n')

# Mapa do labirinto, indicando também suas coordenadas pelas chaves e paredes pelos respectivos valores
mapa_labirinto = labirinto().maze_map
print(f'Mapa: {mapa_labirinto}\n')

# O melhor caminho, caminho perfeito
caminho_perfeito = labirinto().path
print(f'Caminho perfeito: {caminho_perfeito}\n')

# Parametro loop porcent, um labirinto perfeito possui um único caminho para saída, i.e, loopPercent = 0...
