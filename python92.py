jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
n = int(input('Quantos jogos ele jogou? '))
for i in range(0, n):
    jogador[f'partida {i+1}'] = int(input(f'Quantos gol(s) {jogador["nome"]} fez na partida {i+1}: '))
print(f'\n\033[1m{"DESEMPENHO":^35}\033[m\n', '='*35)
gols = []
for k, v in jogador.items():
    if k == 'nome':
        print(f'O jogador {v} jogou {n} partidas.')
    else:
        print(f'=> Na {k}, fez {v} gol(s).')
        gols.append(v)
print(f'Foi um total de {sum(gols)} gol(s).')

