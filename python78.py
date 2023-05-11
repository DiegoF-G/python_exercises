num = []
while True:
    n = float(input('Digite um número: '))
    if n in num:
        print('Número já digitado anteriormente...não será salvo novamente.')
    else:
        num.append(n)
    c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    while c not in 'sSnN':
        c = input('Deseja continuar digitando mais números (S/N)? ').strip()[0]
    if c in 'nN':
        break
num.sort()
print(f'A lista formada pelos números digitados, em ordem crescente, foi: {num}')





