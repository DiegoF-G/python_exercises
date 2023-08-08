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


def cadastrar(arq, nome='desconhecido', idade=0):
    """
    ->Função que escreve no arquivo passado como parâmetro nome e idade de pessoas. Registra como "desconhecido"
      caso não seja inserido o nome e como 0 caso não seja inserido a idade.
    :param arq: string, como o nome do arquivo
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
            print('Houve um ERRO na de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

