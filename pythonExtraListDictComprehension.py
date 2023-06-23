# Nesse arquivo vou explorar as estruturas do List e Dict Comprehension, sendo uma ferramenta do Py para criar listas
# de maneira mais prática e concisa a partir de outras listas.
# Também vou utilizar a função built-in zip para criar listas de tuplas, muito útil para iterações.

# (1)Função que recebe uma lista de floats e devolve uma lista com os respectivos dobros
def lista_dobro(lista: list = None) -> list:
    """
    ->Função que recebe uma lista de números e devolve uma lista com os respectivos dobros.
    :param lista: lista de floats ou inteiros
    :return: lista com os respectivos dobros da lista dada como parâmetro ou a lista [0] caso não seja dado nennhum
    parâmetro
    """
    if lista is None:
        lista = [0]
    lista2x = [x*2 for x in lista]
    return lista2x


teste1 = (print('TESTE 1'), print(lista_dobro([10, 150, 1000, 10.5, 0.75])), print(lista_dobro()), print())

# (2)Uma lista gerada por uma list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro
# elemento seja 'Apartamento':
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
apAluguel = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']
teste2 = (print('TESTE 2'), print(apAluguel), print())

# (3)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
despesasAno = {meses[i]: despesa[i] for i in range(12)}
teste3 = (print('TESTE 3'), print(despesasAno), print())

# (4)Foi repassado uma lista de 20 estudantes e suas respectivas médias finais. Precisamos
# selecionar estudantes que tenham média final maior ou igual a 9.0
nomesEstudantes = ['Enrico Monteiro', 'Luna Pereira', 'Anthony Silveira', 'Letícia Fernandes',
                   'João Vitor Nascimento', 'Maysa Caldeira', 'Diana Carvalho', 'Mariane da Rosa',
                   'Camila Fernandes', 'Levi Alves', 'Nicolas da Rocha', 'Amanda Novaes',
                   'Laís Moraes', 'Letícia Oliveira', 'Lucca Novaes', 'Lara Cunha',
                   'Beatriz Martins', 'João Vitor Azevedo', 'Stephany Rosa', 'Gustavo Henrique Lima']
mediasEstudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5, 8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 6.7, 8.2]
bolsistas = {nome: media for nome, media in zip(nomesEstudantes, mediasEstudantes) if media >= 9.0}
teste4 = (print('TESTE 4'), print(bolsistas))
