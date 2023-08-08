while True:
    n = (int(input('Digite o primeiro número inteiro: ')), int(input('Digite o segundo número inteiro: ')),
          int(input('Digite o terceiro número inteiro: ')), int(input('Digite o quarto número inteiro: ')),
          int(input('Digite o quinto número inteiro: ')))
    p = 0
    for i in range(0, len(n)):
        if n[i] % 2 == 0:
            p += 1
    print(f'\nO número 9 ocorreu {n.count(9)} vez(es).')
    if 3 in n:
        print(f'O número 3 ocorreu primeiro na {n.index(3)} posição.')
    else:
        print('O valor 3 não foi digitado.')
    print(f'Ocorreram {p} número(s) par(es).\n ')
    c = input('Deseja digitar novamente 5 inteiros (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja digitar novamente 5 inteiros (S/N)? ').strip()[0]
    if c in 'nN':
        break
