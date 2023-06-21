palavras = (input('Digite a primeira palavra: ').strip().upper(),
            input('Digite a segunda palavra: ').strip().upper(),
            input('Digite a terceira palavra: ').strip().upper(),
            input('Digite a quarta palavra: ').strip().upper(),
            input('Digite a quinta palavra: ').strip().upper())
for palavra in palavras:
    print(f'\nA palavra {palavra} possui as vogais:', end=' ')
    vogais = ('A', 'E', 'I', 'O', 'U', 'À', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ã', 'Õ', 'Â', 'Ê', 'Î', 'Ô', 'Û')
    for letra in palavra:
        if letra in vogais:
            print(f'"{letra.lower()}"', end=' ')



