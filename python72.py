print('\033[1mBrasileirão 2023 Primeira semana de Maio\033[m')
colBrasileirao = ('Cruzeiro', 'Botafogo', 'Fortaleza', 'Fluminense', 'Palmeiras', 'Internacional', 'Grêmio', 'Vasco',
                  'São Paulo', 'Atlético-MG', 'Cuiabá', 'Santos', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia',
                  'Goiás', 'Corinthians', 'Coritiba', 'América-MG')
print(f'Os cinco primeiros colocados são: {colBrasileirao[:5]}')
print(f'Os quatro últimos colocados são: {colBrasileirao[len(colBrasileirao)-4:len(colBrasileirao)]}')
print(f'Em ordem alfabética, os times do Brasileirão 2023 são: {sorted(colBrasileirao)}')
print(f'Do último colocado ao primeiro: {colBrasileirao[::-1]}')
print(f'O Vasco está na {colBrasileirao.index("Vasco")}ª posição')








