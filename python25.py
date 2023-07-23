frase = ' '.join(input('Escreva uma frase: ').strip().upper().split())
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A aparece na posição {frase.find("A")}')
print(f'A última letra A aparece na posição {frase.rfind("A")}')
# print(f'A última letra A aparece na posição {(len(frase) - frase[::-1].find("A")}')




