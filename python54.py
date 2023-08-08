n = int(input('Digite quantos números serão analisados: '))
p_maior = p_menor = 0
for i in range(1, n+1):
    p = float(input(f'{i}ª valor: '))
    if i == 1:
        p_maior = p
        p_menor = p
    elif p > p_maior:
        p_maior = p
    elif p < p_menor:
        p_menor = p
print(f'O maior valor digitado foi {p_maior} e o menor foi {p_menor}')
