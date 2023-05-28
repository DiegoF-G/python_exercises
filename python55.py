print('-'*5, '\033[1mANALISADOR DE GRUPO\033[m', '-'*5)
n = int(input('Digite quantas pessoas tem no grupo: '))
somaIdade = idadeMaiorM = idadeMaiorF = menorM = menorF = 0
nomeMaisVelho = nomeMaisVelha = ''
if n > 0:
    for j in range(1, n+1):
        print('-'*3, f'{j}ª Pessoa', '-'*3)
        nome = ' '.join(input('Nome: ').strip().title().split())
        idade = int(input('Idade: '))
        sexo = input('Sexo (M/F): ').strip().upper()[0]
        somaIdade += idade
        if j == 1 and sexo == 'M':
            idadeMaiorM = idade
            nomeMaisVelho = nome
        elif j == 1 and sexo == 'F':
            idadeMaiorF = idade
            nomeMaisVelha = nome
        elif idade > idadeMaiorM and sexo == 'M':
            idadeMaiorM = idade
            nomeMaisVelho = nome
        elif idade > idadeMaiorF and sexo == 'F':
            idadeMaiorF = idade
            nomeMaisVelha = nome
        if idade < 21 and sexo == 'M':
            menorM += 1
        if idade < 21 and sexo == 'F':
            menorF += 1
    print('\nAnalisando o grupo informado, temos que:')
    print(f'-A idade média do grupo informado é de {somaIdade/n:.0f} anos.')
    print(f'-{nomeMaisVelho} é o mais velho do grupo, com {idadeMaiorM} anos.')
    print(f'-{nomeMaisVelha} é a mais velha do grupo, com {idadeMaiorF} anos.')
    if menorM > 0:
        print(f'-Ao todo são {menorM} homem(ns) com menos de 21 anos.')
    if menorF > 0:
        print(f'-Ao todo são {menorF} mulher(es) com menos de 21 anos.')
else:
    print('\033[0:31mNúmero de pessoas inválido\033[m')

















