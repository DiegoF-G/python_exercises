coresFortes = {'limpa': '\033[m', 'verde': '\033[1:32m', 'vermelho': '\033[1:31m', 'branco': '\033[1m'}
alunos = list()
while True:
    aluno = {'nome': input('Nome: '), 'nota1': float(input('Nota na P1: ')), 'nota2': float(input('Nota na P2: '))}
    aluno['media'] = (aluno["nota1"] + aluno["nota2"]) / 2
    if aluno['media'] >= 7:
        aluno['situacao'] = f'{coresFortes["verde"]}Aprovado(a)!{coresFortes["limpa"]}'
    elif aluno['media'] >= 5:
        aluno['situacao'] = f'{coresFortes["branco"]}Recuperação.{coresFortes["limpa"]}'
    else:
        aluno['situacao'] = f'{coresFortes["vermelho"]}Reprovado(a).{coresFortes["limpa"]}'
    alunos.append(aluno.copy())
    c = input('Deseja continuar informando mais alunos (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar informando mais alunos (S/N)? ').strip()[0]
    if c in 'nN':
        break
print(f'\n{coresFortes["branco"]}Panorama geral dos alunos:{coresFortes["limpa"]}')
for i, aluno in enumerate(alunos):
    a = (print(f'\nNo.{i}'), print(f'-Nome: {aluno["nome"]}'), print(f'-Média: {aluno["media"]:.1f}'),
         print(f'-Situação: {aluno["situacao"]}'))











