def linha(l=42, c='-'):
    """
    ->Função que fornece uma linha de tamanho dado pelo primeiro parâmetro, o tamanho padrão são de 42 caractéres "-".
    :param l: inteiro, sendo o tamanho da linha
    :param c: string, sendo o caractér a ser colocado em linha na quanditade dada pelo parâmetro l
    :return: string
    """
    return l*c


def cabecalho(txt, c=42):
    """
    ->Função que fornece um cabeçalho com texto dado pelo parâmetro, alinhado por padrão em 42 caractéres.
    :param txt: string, sendo o texto a constar no cabeçalho
    :param c: inteiro, sendo em quantos espaços o texto vai estar alinhado
    :return: string, sendo o cabeçalho completo ocupando 3 linhas
    """
    t = (print(linha()), print(txt.center(c)), print(linha()))
    return t


def menu(lista):
    """
    ->Função que printa um menu de acordo com os itens inseridos em seu parâmetro na forma de uma lista, em sequência.
      Além disso, solicita ao usuário digitar a opção desejada na forma de um inteiro correspondente ao item
      (índice dele) na lista.
    :param lista: uma lista (array), onde cada entrada dele é um item do menu desejado
    :return: string, que corresponde a uma solicitação de qual opção o usuário deseja selecionar pelo índice da opção
    """
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[34m{item}\033[m')
    opc = leia_int('Sua opção: ')
    return opc