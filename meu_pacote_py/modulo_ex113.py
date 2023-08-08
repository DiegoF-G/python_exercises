# modularição do exercício 113, o último do curso


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
    ->Função que fornece uma linha de caractéres "-" de tamanho dado pelo primeiro parâmetro,
      o tamanho padrão são de 42 caractéres "-".
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
    :return: função sem retorno
    """
    t = (print(linha(c)), print(txt.center(c)), print(linha(c)))


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


def arquivo_existe(nome):
    """
    ->Função que verifica se um arquivo existe na pasta.
    :param nome: string, como o nome do arquivo
    :return: booleano, True para a presença do arquivo e False caso contrário
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    ->Função que cria um arquivo com nome dado pelo parâmetro na pasta. Printa caso o arquivo seja criado ou não.
    :param nome: string, como o nome do arquivo
    :return: função sem retorno
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    """
    ->Função que lê um arquivo e o exibe, printando se foi lido com sucesso ou não.
    :param nome: string, como o nome do arquivo
    :return: função sem retorno
    """
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()


def formatar_nome(nome):
    """
    ->Função que recebe nome (espera-se ser de uma pessoa) em forma de string e formata colocando letras iniciais
      maiúsculas e removendo espaços desnecessários.
    :param nome: string, sendo o nome de uma pessoa
    :return: string, sendo o nome formatado
    """
    name = ' '.join(nome.strip().title().split())
    return name


def cadastrar(arq, nome='desconhecido', idade=0):
    """
    ->Função que escreve no arquivo txt passado como parâmetro nome e idade de pessoas. Registra como "desconhecido"
      caso não seja inserido o nome e como 0 caso não seja inserido idade. O nome é formatado de forma usual
      (iniciais maiúsculas e sem "espaços desnecessários") e em idade só é permitido como um número inteiro.
    :param arq: string, como o nome do arquivo txt
    :param nome: string, como o nome de uma pessoa
    :param idade: interio, sendo a idade da pessoa
    :return: função sem retorno
    """
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}\t\t{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
