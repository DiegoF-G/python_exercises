nome_completo = input('Digite seu nome completo: ').strip().title().split()
print(f'Prazer em te conhecer!')
print(f'Seu primeiro nome é {nome_completo[0]} \nSeu último nome é {nome_completo[len(nome_completo) - 1]}')
