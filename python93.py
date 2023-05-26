cores = {'limpa': '\033[m', 'vermelho': '\033[0:31m', 'brancoForte': '\033[1m'}
print(f'{cores["brancoForte"]}CADASTRAMENTO{cores["limpa"]}')
grupo = list()
s = 0
while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo (M/F): ').strip()[0]
    while pessoa['sexo'] not in 'mMfF':
        print(f'{cores["vermelho"]}Dado inválido! Favor digite novamente.{cores["limpa"]}')
        pessoa['sexo'] = input('Sexo (M/F): ').strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    grupo.append(pessoa.copy())
    c = input('Deseja continuar informando mais pessoas (S/N)? ').strip()[0]
    while c not in 'sSnN':
        print(f'{cores["vermelho"]}Resposta inválida! Favor digite novamente.{cores["limpa"]}')
        c = input('Deseja continuar informando mais pessoas (S/N)? ').strip()[0]
    if c in 'nN':
        break
m = s / len(grupo)
mulheres = []
acimaMedia = []
for pessoa in grupo:
    if pessoa['sexo'] in 'fF':
        mulheres.append(pessoa['nome'])
    if pessoa['idade'] > m:
        acimaMedia.append(pessoa)
print(f'{"-="*35}\nA) Foram {len(grupo)} pessoas cadastradas.\nB) A média de idade é de {m:.0f} anos.')
if len(mulheres) > 0:
    print('C) As mulheres cadastradas foram', end=' ')
    for mulher in mulheres:
        if mulher != mulheres[len(mulheres) - 1]:
            print(f'{mulher},', end=' ')
        else:
            print(f'{mulher}.')
else:
    print('C) Nenhuma mulher foi cadastrada.')
if len(acimaMedia) > 0:
    print('D) Lista de pessoas com idade acima da média:')
    for acima in acimaMedia:
        for k, v in acima.items():
            if k != 'idade':
                print(f'{k}: {v};', end=' ')
            else:
                print(f'{k}: {v}')
else:
    print(f'D) Todos cadastrados possuem a mesma idade, de {m:.0f} anos.')









