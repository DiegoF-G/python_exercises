# Nesse arquivo vou explorar o uso da função built-in map, que recebe uma lista e aplica em cada entrada dela outra
# função que pode ser anônima (função lambda) ou outra definida breviamente.

# (1)Função que recebe uma lista de números e retorna uma lista do triplo dos respectivos números
def lista_triplo(lista: list = None) -> list:
    """
    ->Função que recebe uma lista de números e retorna uma lista com os respectivos triplos desses números.
    :param lista: lista de floats ou inteiros
    :return: lista com os triplos dos números em cada índice da lista de entrada, respectivamente, ou a lista [0] caso
    não seja passado nenhum parâmetro
    """
    if lista is None:
        lista = [0]
    return list(map(lambda x: 3*x, lista))


teste1 = (print('Teste 1'), print(lista_triplo([1, 2, 3, 4, 0.1, 0.005, 10.3333])), print(lista_triplo()), print())


# (2)Função que recebe uma lista de temperaturas em graus Celsius e transforma numa lista de temperatura em Fahrenheit
def lista_fahrenheit(lista_c: list = None) -> list:
    """
    ->Função que recebe uma lista de medidas de temperaturas em Celsius e transforma numa lista das mesmas em Fahrenheit.
    :param lista_c: lista de floats ou inteiros, sendo a lista de medidas de temperaturas em Celsius
    :return: lista das mesmas medidas de temperaturas, respectivamente, em Fahrenheit ou uma lista vazia caso não seja
    passado nenhum parâmetro
    """
    if lista_c is None:
        lista_c = []
    return list(map(lambda tc: (tc * 9 / 5) + 32, lista_c))


teste2 = (print('Teste 2'), print(lista_fahrenheit([0, 25, 37, 78, 100])), print(lista_fahrenheit()), print())


# (3)Função que recebe uma lista de números e retorna uma lista dos quadrados dos respectivos números
def lista_quadrado(lista: list = None) -> list:
    """
    ->Função que recebe uma lista de números e retorna uma lista com os respectivos quadrados desses números.
    :param lista: lista de floats ou inteiros
    :return: lista com os quadrados dos números em cada índice da lista de entrada, respectivamente, ou a lista [0]
    caso não seja passado nenhum parâmetro
    """
    if lista is None:
        lista = [0]
    return list(map(lambda x: x**2, lista))


teste3 = (print('Teste 3'), print(lista_quadrado([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.5, 0.05])), print(lista_quadrado()),
          print())


# (4)Uma função que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho
# maior ou igual a 5, exibindo-as numa lista. Aqui usarei a função built-in Filter.
def palavra_com_mais_de_5_letras_em_(frase: str = '') -> list:
    """
    ->Função que recebe uma frase e retorna uma lista com as palavras que possuem mais de 5 letras.
    :param frase: string, sendo uma frase qualquer
    :return: lista, das palavras com 5 letras ou mais, ou uma lista vazia caso não seja passado nenhum parâmetro
    """
    if type(frase) != str:
        raise Exception(f'{AttributeError}: Ops! Você não digitou uma frase literal (string) no argumento da função.')
    frase_formatada = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()
    return list(filter(lambda palavra: len(palavra) >= 5, frase_formatada))


teste4 = (print('Teste 4'), print(palavra_com_mais_de_5_letras_em_('Aprender Python aqui na Alura é muito bom')),
          print(palavra_com_mais_de_5_letras_em_('TESTE??!!')), print(palavra_com_mais_de_5_letras_em_()))
