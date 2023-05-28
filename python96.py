def printar_em_destaque(m):
    msg = ' '.join(m.strip().split())
    print('-'*(len(msg) + 4))
    print(f'  \033[1m{msg}\033[m')
    print('-'*(len(msg) + 4))


mensagem = input('Escreva uma mensagem qualquer para ser printada em destaque: ')
printar_em_destaque(mensagem)

