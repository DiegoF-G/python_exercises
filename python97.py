cores = {'limpa': '\033[m', 'vermelho': '\033[0:31m', 'brancoForte': '\033[1m'}


def contagem(c, f, p):
    if c <= f and p > 0:
        for i in range(c, f + 1, p):
            if p <= abs(i - f):
                print(f'{i} -> ', end='')
            else:
                print(i)
    elif c >= f and p > 0:
        for i in range(c, f - 1, -p):
            if p <= abs(i - f):
                print(f'{i} -> ', end='')
            else:
                print(i)
    elif c >= f and p < 0:
        for i in range(c, f - 1, p):
            if -p <= abs(i - f):
                print(f'{i} -> ', end='')
            else:
                print(i)
    elif c <= f and p == 0:
        for i in range(c, f + 1):
            if i != f:
                print(f'{i} -> ', end='')
            else:
                print(i)
    elif c > f and p == 0:
        for i in range(c, f - 1, -1):
            if i != f:
                print(f'{i} -> ', end='')
            else:
                print(i)
    else:
        print(f'{cores["vermelho"]}Contagem inválida!{cores["limpa"]}')


def escrever_em_destaque(m):
    msg = ' '.join(m.strip().split())
    print('-'*(len(msg) + 4))
    print(f'  \033[1m{msg}\033[m')
    print('-'*(len(msg) + 4))


escrever_em_destaque('CONTAGEM')
while True:
    comeco = int(input('\nQual o primeiro número da contagem: '))
    fim = int(input('Qual o último número da contagem: '))
    passo = int(input('Passo da contagem: '))
    if passo != 0:
        print(f'\n{cores["brancoForte"]}Contagem de {comeco} a {fim} de {passo} em {passo}:{cores["limpa"]}')
    else:
        print(f'\n{cores["brancoForte"]}Contagem de {comeco} a {fim} de 1 em 1:{cores["limpa"]}')
    contagem(comeco, fim, passo)
    r = input('\nDeseja realizar outra contagem (S/N)? ').strip()[0]
    while r not in 'sSnN':
        r = input('Deseja realizar outra contagem (S/N)? ').strip()[0]
    if r in 'nN':
        break






