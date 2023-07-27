from collections import defaultdict, Counter

# Frase com palavras repetidas de propósito
frase = "Meu nome é Diego e gosto de nome e gosto de cachorros de SP"

# Dicionário padrão (default dict) usado para verificar a frequência das palavras numa frase (string transformada em lista)
aparicoes = defaultdict(int)
for palavra in frase.split():
    aparicoes[palavra] += 1  # em vez de usar aparicoes.get(palavra, 0), devido ao defaultdict.

print(aparicoes)
print(type(aparicoes))

print()

# Outra forma de contar numa lista e transformar em dicionário e pela classe "Counter" do pacote "collections"
aparicoes = Counter(frase.split())
print(aparicoes)
print(type(aparicoes))
