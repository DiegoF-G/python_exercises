jogador = dict()
jogador['nome'] = input('Nome do jogador(a): ')
n = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
s = 0
for i in range(0, n):
    jogador[f'partida {i+1}'] = int(input(f'Quantos gol(s) ele(a) fez na partida {i+1}: '))
    s += jogador[f'partida {i+1}']
jogador['total'] = s
print(f'\n\033[1m{"DESEMPENHO":^35}\033[m\n', '='*35)
for k, v in jogador.items():
    if k == 'nome':
        print(f'O(a) jogador(a) {v} jogou {n} partida(s).')
    elif k != 'nome' != 'total' != k:
        print(f'=> Na {k}, fez {v} gol(s).')
    else:
        print(f'Foi um {k} de {v} gol(s).')


