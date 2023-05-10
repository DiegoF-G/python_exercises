palavras = (input('Digite a primeira palavra: ').strip().upper(),
            input('Digite a segunda palavra: ').strip().upper(),
            input('Digite a terceira palavra: ').strip().upper(),
            input('Digite a quarta palavra: ').strip().upper(),
            input('Digite a quinta palavra: ').strip().upper())
for p in palavras:
    print(f'\nA palavra {p} possui as vogais:', end=' ')
    vogais = ('A', 'E', 'I', 'O', 'U', 'À', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â', 'Ê', 'Î', 'Ô', 'Û')
    for letra in p:
        if letra in vogais:
            print(f'"{letra.lower()}"', end=' ')



