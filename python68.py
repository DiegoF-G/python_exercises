print('\033[1mCADASTRO DE PESSOAS\033[m')
i = j = k = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Preenchimento inválido, favor digite novamente o sexo (M/F): ').strip().upper()[0]
    if idade >= 18:
        i += 1
    if sexo == 'M':
        j += 1
    if sexo == 'F' and idade < 20:
        k += 1
    c = input('Deseja continuar (S/N)? ').strip().upper()[0]
    while c not in 'SN':
        c = input('Deseja continuar (S/N)? ').strip().upper()[0]
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {i}\nTotal de homens: {j}\nTotal de mulheres com menos de 20 anos: {k}')




