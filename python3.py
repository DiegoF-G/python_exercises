x = input('Digite algo: ')
print(f'\nSó tem espaços: {x.isspace()}\nÉ numérico: {x.isnumeric()}\nÉ alfabético: {x.isalpha()}')
print(f'É alfanumérico: {x.isalnum()}\nEstá em maiúsculo: {x.isupper()}\nEstá em minúsculo: {x.islower()}')
print(f'Está capitalizado (começa com maiúsculo): {x.istitle()}')


