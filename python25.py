frase = input('Escreva uma frase: ').strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}')
print(f'A última letra A aparece na posição {frase.rfind("A") + 1}')
# print(f'A ultima letra A aparece na posição {(len(frase) - frase[::-1].find("A")}')




