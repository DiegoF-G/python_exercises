r = input('Digite qual é seu sexo(M/F): ').strip()[0]
while r not in 'mMfF':
    print('Opção inválida, digite novamente!')
    r = input('Digite qual é seu sexo(M/F): ').strip()[0]
print('Sexo registado com sucesso!')
