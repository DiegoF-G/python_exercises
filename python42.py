print('\033[1mAnálise de IMC\033[m')
m = float(input('Qual seu peso? '))
h = float(input('Qual a sua altura? '))
IMC = m/h**2
if IMC < 18.5:
    print('Você está \033[1mabaixo do peso\033[m')
elif IMC < 25:
    print('Você está com o \033[1mpeso ideal\033[m!')
elif IMC < 30:
    print('Você está com \033[1msobrepeso\033[m')
elif IMC < 40:
    print('Você está em \033[1mobesidade\033[m, cuidado!')
else:
    print('Você está em \033[1mobesidade mórbida\033[m, muito cuidado!')