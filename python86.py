from numpy.linalg import det
print('\033[4:34mMATRIZ E DETERMINANTE\033[m')
axis = (int(input('Digite quantas LINHAS terá sua matriz: ')), int(input('Digite quantas COLUNAS terá sua matriz: ')))
matrix = []
for i in range(0, axis[0]):
    matrix.append([])
sPares = sTerceiraC = 0
for i in range(0, axis[0]):
    for j in range(0, axis[1]):
        m = float(input(f'\nDigite um número para a entrada \033[1m[{i+1}, {j+1}]\033[m da matriz: '))
        if m % 2 == 0:
            sPares += m
        if j == 2:
            sTerceiraC += m
        matrix[i].append(m)
print('\n\033[1:34mMatriz:\033[m ', end='')
for i in range(0, axis[0]):
    if i == 0:
        print(matrix[i])
    else:
        print(' '*7, matrix[i])
tr = 0
if axis[0] == axis[1] and axis[0] > 0:
    print(f'\033[1:34mDeterminante:\033[m {det(matrix)}')
    for i in range(0, axis[0]):
        tr += matrix[i][i]
    print(f'\033[1:34mTraço:\033[m {tr}')
print(f'A soma de todos números pares na matriz é {sPares}.\nA soma de todos números da terceira coluna é {sTerceiraC}.')
print(f'O maior número da segunda linha é {max(matrix[1])}.')









