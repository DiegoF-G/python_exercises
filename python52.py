print('\033[1mIdentificador de Palíndromo\033[m')
f = input('Digite uma frase (sem acentuações ou "ç"): ').strip().upper()
frase = ''.join(f.split())
fraseI = frase[::-1]
if fraseI == frase:
    print(f'A frase "{frase}" ao contrário é "{fraseI}". Portanto a frase digitada é um \033[1mpalíndromo\033[m!')
else:
    print(f'A frase "{frase}" ao contrário é "{fraseI}". Portanto a frase digitada \033[1mnão\033[m é um palíndromo.')
# f = input('Digite uma frase (sem acentuações ou "ç"): ').strip().upper()
# frase = ''.join(f.split())
# fraseI = ''
# for i in range(len(frase)-1, -1, -1):
#     fraseI += frase[i]
# if fraseI == frase:
#     print(f'A frase "{frase}" ao contrário é "{fraseI}". Portanto a frase digitada é um \033[1mpalíndromo\033[m!')
# else:
#    print(f'A frase "{frase}" ao contrário é "{fraseI}". Portanto a frase digitada \033[1mnão\033[m é um palíndromo.')









