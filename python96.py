def escrever_em_destaque(m):
    msg = ' '.join(m.strip().split())
    print('-'*(len(msg) + 4))
    print(f'  \033[1m{msg}\033[m')
    print('-'*(len(msg) + 4))


mensagem = input('Escreva uma mensagem qualquer para ser exposta em destaque: ')
escrever_em_destaque(mensagem)
escrever_em_destaque('      CURSO EM VÍDEO         PYTHON MUNDO 3')

