x = input('Digite algo: ')
print(f'Tipo do valor digitado: {type(x)} \n Só é espaços: {x.isspace()} \n É numérico: {x.isnumeric()} \n É alfabético: {x.isalpha()} \n É alfanumérico: {x.isalnum()} \n Está em maíusculo: {x.isupper()} \n Está em mínusculo: {x.islower()} \n Está capitalizado (começa com maiúsculo): {x.istitle()}')

