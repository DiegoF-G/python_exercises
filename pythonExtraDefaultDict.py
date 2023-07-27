from collections import defaultdict

# Frase com palavras repetidas de propósito
frase = "Meu nome é Diego e gosto de nome e gosto de cachorros de SP"

# Dicionário padrão usado para verificar a frequência das palavras numa frase (string transformada em lista)
aparicoes = defaultdict(int)
for palavra in frase.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)
print(type(aparicoes))
