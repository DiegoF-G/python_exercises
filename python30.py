d = float(input('Qual a distância de sua viagem, em km: '))
print(f'O valor de sua viagem é de R${d*0.5:.2f}' if d<=200 else f'O valor de sua viagem é de R${d*0.45:.2f}')

# R$0,50/km quando d<=200 e R$0.45/km para viagens mais longas
