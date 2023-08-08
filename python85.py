from numpy.linalg import det
print('\033[4:34mMATRIZ E DETERMINANTE\033[m')
axi = (int(input('Digite quantas LINHAS terá sua matriz: ')), int(input('Digite quantas COLUNAS terá sua matriz: ')))
matrix = []
for i in range(0, axi[0]):
    matrix.append([])
for i in range(0, axi[0]):
    for j in range(0, axi[1]):
        matrix[i].append(float(input(f'\nDigite um número para a entrada \033[1m[{i+1}, {j+1}]\033[m da matriz: ')))
print('\n\033[1:34mMatriz:\033[m ', end='')
for i in range(0, axi[0]):
    if i == 0:
        print(matrix[i])
    else:
        print(' '*7, matrix[i])
if axi[0] == axi[1] and axi[0] > 0:
    print(f'\033[1:34mDeterminante:\033[m {det(matrix)}')
