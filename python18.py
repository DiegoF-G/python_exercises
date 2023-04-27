from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
a5 = input('Quinto aluno: ')
list = [a1, a2, a3, a4, a5]
escolhido = choice(list) #random.choice(list) if import random
print(f'O aluno escolhido foi: {escolhido}')



