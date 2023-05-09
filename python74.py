p = 0
while True:
    nT = (int(input('Digite o primeiro número inteiro: ')), int(input('Digite o segundo número inteiro: ')),
          int(input('Digite o terceiro número inteiro: ')), int(input('Digite o quarto número inteiro: ')),
          int(input('Digite o quinto número inteiro: ')))
    for i in range(0, len(nT)):
        if nT[i] % 2 == 0:
            p += 1
    print(f'\nO número 9 ocorreu {nT.count(9)} vez(es).')
    if 3 in nT:
        print(f'O número 3 ocorreu primeiro na {nT.index(3)} posição.')
    else:
        print('O valor 3 não foi digitado.')
    print(f'Ocorreram {p} número(s) pare(s).\n ')
    c = input('Deseja digitar novamente 5 inteiros (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja digitar novamente 5 inteiros (S/N)? ').strip()[0]
    if c in 'nN':
        break










