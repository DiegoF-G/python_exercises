print('-=-'*10, '\033[1:32mAnalisador de Triângulos\033[m', '-=-'*10)

n1 = float(input('Medida do primeiro segmento de reta: '))
n2 = float(input('Medida do segundo segmento de reta: '))
n3 = float(input('Medida do terceiro segmento de reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os segmentos de reta mencionados \033[0:32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos de reta mencionados \033[0:31mNÃO PODEM FORMAR\033[m um triângulo!')



