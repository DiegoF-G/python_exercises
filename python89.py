cores_fortes = {'limpa': '\033[m', 'verde': '\033[1:32m', 'vermelho': '\033[1:31m', 'branco': '\033[1m'}
alunos = list()
while True:
    aluno = {'nome': input('Nome: '), 'nota1': float(input('Nota na P1: ')), 'nota2': float(input('Nota na P2: '))}
    aluno['media'] = (aluno["nota1"] + aluno["nota2"]) / 2
    if aluno['media'] >= 7:
        aluno['situacao'] = f'{cores_fortes["verde"]}Aprovado(a)!{cores_fortes["limpa"]}'
    elif aluno['media'] >= 5:
        aluno['situacao'] = f'{cores_fortes["branco"]}Recuperação.{cores_fortes["limpa"]}'
    else:
        aluno['situacao'] = f'{cores_fortes["vermelho"]}Reprovado(a).{cores_fortes["limpa"]}'
    alunos.append(aluno.copy())
    c = input('Deseja continuar informando mais alunos (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar informando mais alunos (S/N)? ').strip()[0]
    if c in 'nN':
        break
print(f'\n{cores_fortes["branco"]}Panorama geral dos alunos:{cores_fortes["limpa"]}')
for i, aluno in enumerate(alunos):
    a = (print(f'\nNo.{i}'), print(f'-Nome: {aluno["nome"]}'), print(f'-Média: {aluno["media"]:.1f}'),
         print(f'-Situação: {aluno["situacao"]}'))
