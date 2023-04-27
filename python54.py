n = int(input('Digite quantos números serão analisados: '))
pmaior = 0
pmenor = 0
for i in range(1, n+1):
    p = float(input(f'{i}ª valor: '))
    if i == 1:
        pmaior = p
        pmenor = p
    elif p > pmaior:
        pmaior = p
    elif p < pmenor:
        pmenor = p
print(f'O maior valor digitado foi {pmaior} e o menor foi {pmenor}')










