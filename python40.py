from datetime import date
print('\033[1:34mClassificação de Atletas de Natação\033[m')
b = int(input('Qual o seu ano de nascimento: '))
y = date.today().year - b
if y <= 9:
    print(f'O(a) atleta tem {y} anos\nClassificação: Mirim')
elif y <= 14:
    print(f'O(a) atleta tem {y} anos\nClassificação: Infantil')
elif y <= 19:
    print(f'O(a) atleta tem {y} anos\nClassificação: Junior')
elif y <= 25:
    print(f'O(a) atleta tem {y} anos\nClassificação: Sênior')
else:
    print(f'O(a) atleta tem {y} anos\nClassificação: Master')


