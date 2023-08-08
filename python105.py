cores = {'limpa': '\033[m', 'fundoVermelho': '\033[0:41m', 'py': '\033[1:34:43m', 'brancoInverso': '\033[7m'}


def titulo(m, cor=cores['limpa'], sim='~'):
    t = (print(cor, end=''), print(sim*(len(m) + 4)), print('  ' + m), print(sim*(len(m) + 4)), print(cores['limpa']))


def ajuda(c):
    titulo(f'Acessando o manual do comando {comando}:', sim='-')
    a = (print(cores['brancoInverso']), help(c), print(cores['limpa']))


while True:
    titulo('Sistema de Ajuda PyHELP', cores['py'])
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Obrigado e volte sempre!', cores['fundoVermelho'])
