print('-'*5, '\033[1mANALISADOR DE GRUPO\033[m', '-'*5)
n = int(input('Digite quantas pessoas tem no grupo: '))
soma_idade = idade_maior_m = idade_maior_f = menor_m = menor_f = 0
nome_mais_velho = nome_mais_velha = ''
if n > 0:
    for j in range(1, n+1):
        print('-'*3, f'{j}ª Pessoa', '-'*3)
        nome = ' '.join(input('Nome: ').strip().title().split())
        idade = int(input('Idade: '))
        sexo = input('Sexo (M/F): ').strip().upper()[0]
        soma_idade += idade
        if j == 1 and sexo == 'M':
            idade_maior_m = idade
            nome_mais_velho = nome
        elif j == 1 and sexo == 'F':
            idade_maior_f = idade
            nome_mais_velha = nome
        elif idade > idade_maior_m and sexo == 'M':
            idade_maior_m = idade
            nome_mais_velho = nome
        elif idade > idade_maior_f and sexo == 'F':
            idade_maior_f = idade
            nome_mais_velha = nome
        if idade < 21 and sexo == 'M':
            menor_m += 1
        if idade < 21 and sexo == 'F':
            menor_f += 1
    print('\nAnalisando o grupo informado, temos que:')
    print(f'-A idade média do grupo informado é de {soma_idade/n:.0f} anos.')
    print(f'-{nome_mais_velho} é o mais velho do grupo, com {idade_maior_m} anos.')
    print(f'-{nome_mais_velha} é a mais velha do grupo, com {idade_maior_f} anos.')
    if menor_m > 0:
        print(f'-Ao todo são {menor_m} homem(ns) com menos de 21 anos.')
    if menor_f > 0:
        print(f'-Ao todo são {menor_f} mulher(es) com menos de 21 anos.')
else:
    print('\033[0:31mNúmero de pessoas inválido\033[m')
