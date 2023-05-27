cores = {'limpa': '\033[m', 'vermelho': '\033[0:31m', 'brancoForte': '\033[1m'}
print(f'{cores["brancoForte"]}ANÁLISE DE DESEMPENHO{cores["limpa"]}')
jogadores = list()
while True:
    jogador = dict()
    jogador['Nome'] = input('Nome do jogador(a): ')
    n = int(input(f'Quantos jogos {jogador["Nome"]} jogou? '))
    gols = []
    for i in range(0, n):
        gol = jogador[f'partida {i + 1}'] = int(input(f'Quantos gol(s) ele(a) fez na partida {i + 1}: '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    c = input('Deseja continuar informando mais jogadores (S/N)? ').strip()[0]
    while c not in 'sSnN':
        print(f'{cores["vermelho"]}Resposta inválida! Favor digite novamente.{cores["limpa"]}')
        c = input('Deseja continuar informando mais jogadores(as) (S/N)? ').strip()[0]
    if c in 'nN':
        break
tabela = (print(f'\n{cores["brancoForte"]}Panorama{cores["limpa"]}'), print('No.', end=''))
for k in jogador.keys():
    if k == 'Nome':
        print(f'{k:<15}', end='')
    elif k == 'Gols':
        print(f'{k + "por partida":<40}', end='')
    elif k == 'Total':
        print(f'{k}')
for i, jogador in enumerate(jogadores):
    print(f'{i + 1:<3}', end='')
    for k, v in jogador.items():
        if k == 'Nome':
            print(f'{v:<15}', end='')
        elif k == 'Gols':
            print(f'{str(v):<40}', end='')
        elif k == 'Total':
            print(f'{v}')
print(f'\n{cores["brancoForte"]}Levantamento dos Jogadores{cores["limpa"]}')
while True:
    i = int(input('Ver o desempenho de qual jogador(a) (digite o No. dele(a) ou 999 para encerrar)? '))
    while 999 > i > len(jogadores) or i > 999 or i <= 0:
        print(f'{cores["vermelho"]}Número inválido! Favor digite novamente.{cores["limpa"]}')
        i = int(input('Ver o desempenho de qual jogador(a) (digite o No. dele(a) ou 999 para encerrar)? '))
    if i == 999:
        print(f'{cores["brancoForte"]}Programa encerrado.{cores["limpa"]}')
        break
    for k, v in jogadores[i - 1].items():
        if k == 'Nome':
            print(f'\nO(a) jogador(a) {v} jogou {len(jogadores[i - 1]["Gols"])} partida(s).')
        elif 'partida' in k:
            print(f' => Na {k}, fez {v} gol(s).')
        elif k == 'Total':
            print(f'Foi um total de {v} gol(s).\n')






