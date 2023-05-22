n = int(input('Digite quantos números serão analisados: '))
pMaior = pMenor = 0
for i in range(1, n+1):
    p = float(input(f'{i}ª valor: '))
    if i == 1:
        pMaior = p
        pMenor = p
    elif p > pMaior:
        pMaior = p
    elif p < pMenor:
        pMenor = p
print(f'O maior valor digitado foi {pMaior} e o menor foi {pMenor}')











