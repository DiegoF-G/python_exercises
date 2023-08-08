from datetime import date
k = j = 0
for i in range(1, 8):
    y = int(input(f'Qual o ano de nascimento da {i}ª pessoa? '))
    a = date.today().year - y
    if a > 21:
        k += 1
    else:
        j += 1
print(f'Ao todo tivemos {k} maiores de idade e {j} menores de idade.')
