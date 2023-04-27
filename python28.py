v = int(input('Qual é a velocidade atual do carro, em km/h? '))
if v > 80:
    print(f'Reduza a velocidade! Você foi \033[1:31mMULTADO!!!\033[m Sua multa é no valor de R${(v - 80) * 11},00')
print(f'O limite de velocidade é de 80 km/h. Dirija com pé leve!')

# print(f'São R$11,00 para cada km/h acima do limite de 80 km/h nessa via.')

