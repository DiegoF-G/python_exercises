nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome com todas letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas letras minúsculas: {nome.lower()}')
print(f'Seu nome completo possui {len(nome)-(len(nome.split()) - 1)} letras!')
print(f'Seu primeiro nome possui {len(nome.split()[0])} letras')























