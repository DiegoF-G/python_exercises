print('\033[1mBrasileirão 2023 Primeira semana de Maio\033[m')
col_brasileirao = ('Cruzeiro', 'Botafogo', 'Fortaleza', 'Fluminense', 'Palmeiras', 'Internacional', 'Grêmio', 'Vasco',
                  'São Paulo', 'Atlético-MG', 'Cuiabá', 'Santos', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia',
                  'Goiás', 'Corinthians', 'Coritiba', 'América-MG')
print(f'Os cinco primeiros colocados são: {col_brasileirao[:5]}')
print(f'Os quatro últimos colocados são: {col_brasileirao[len(col_brasileirao)-4:len(col_brasileirao)]}')
print(f'Em ordem alfabética, os times do Brasileirão 2023 são: {sorted(col_brasileirao)}')
print(f'Do último colocado ao primeiro: {col_brasileirao[::-1]}')
print(f'O Vasco está na {col_brasileirao.index("Vasco")}ª posição')
