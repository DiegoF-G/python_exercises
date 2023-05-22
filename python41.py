from math import hypot
print('-=-'*10, '\033[1:32mAnalisador de Triângulos\033[m', '-=-'*10)
n1 = float(input('Medida do primeiro segmento de reta: '))
n2 = float(input('Medida do segundo segmento de reta: '))
n3 = float(input('Medida do terceiro segmento de reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos de reta mencionados \033[0:32mPODEM FORMAR\033[m um \033[1mtriângulo\033[m', end=' ')
    if n1 == n2 == n3:
        print('\033[1mequilatero\033[m', end=' ')
    if n1 == n2 or n1 == n3 or n2 == n3:
        print('\033[1misóceles\033[m', end=' ')
    if n1 != n2 != n3 != n1:
        print('\033[1mescaleno\033[m', end=' ')
    if n1 == hypot(n2, n3) or n2 == hypot(n1, n3) or n3 == hypot(n1, n2):
        print('\033[1mretângulo!\033[m')
    if n1 > hypot(n2, n3) or n2 > hypot(n1, n3) or n3 > hypot(n1, n2):
        print('\033[1mobtusângulo!\033[m')
    if n1 < hypot(n2, n3) and n2 < hypot(n1, n3) and n3 < hypot(n1, n2):
        print('\033[1macutângulo!\033[m')
else:
    print('Os segmentos de reta mencionados \033[0:31mNÃO PODEM FORMAR\033[m um triângulo!')
# a classificação referente a ângulo, acutângulo obtusângulo retângulo,
# é consequência de uma manipulação matemática da lei dos cossenos!


