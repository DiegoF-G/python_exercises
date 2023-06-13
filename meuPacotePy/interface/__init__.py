def leia_int(m='Digite um inteiro: '):
    """
    ->Função que lê um inteiro se, e somente se, a string digitada pode ser convertida no tipo primitivo inteiro.
      No caso de não ser possível essa conversão, é printado uma string informando que o valor é inválido.
      Se a execução for interrompida, retorna o inteiro 0.
    :param m: string, que se espera ser uma mensagem solicitando qual o inteiro em questão
    :return: inteiro, convertido da string se possível a conversão
    """
    while True:
        try:
            n = int(input(m))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__} Ops! O valor digitado não é um inteiro. Favor digite novamente.\033[m')
        except KeyboardInterrupt as erro:
            print(f'\n\033[0:31m{erro.__class__} O usuário interrompeu a execução.\033[m')
            return 0
        else:
            return n


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