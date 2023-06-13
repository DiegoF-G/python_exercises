# pasta usada como pacote (pack) referente aos exercícios 106 ao 110


def dobro(f=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece o dobro de um número.
    :param f: float de entrada
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o dobro do float de entrada
    """
    return 2*f if monetario is False else moeda(2*f, m=unidade)


def metade(f=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece a metade de um número.
    :param f: float de entrada
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é a metade do float de entrada
    """
    return 0.5*f if monetario is False else moeda(0.5*f, m=unidade)


def aumentar(f=0.0, a=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece um número aumentado por um determinado acréscimo porcentual.
    :param f: float que representa o número a receber um acréscimo porcentual
    :param a: float que representa o acréscimo porcentual
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o parametro f acrescido porcentualmente pelo parametro a
    """
    return (1+(a/100))*f if monetario is False else moeda((1+(a/100))*f, m=unidade)


def diminuir(f=0.0, d=0.0, monetario=False, unidade='US$'):
    """
    ->Função que fornece um número diminuído por um determinado descréscimo porcentual.
    :param f: float que representa o número a receber um descréscimo porcentual
    :param d: float que representa o descréscimo porcentual
    :param monetario: booleano que determina se resultado vai ser formatado pela função moeda()
    :param unidade: string referente a unidade monetária a ser passada para a função moeda(), por padrão o dolár
    :return: float que é o parametro f descrescido porcentualmente pelo parametro a
    """
    return (1-(d/100))*f if monetario is False else moeda((1-(d/100))*f, m=unidade)


def moeda(f=0.0, m='US$'):
    """
    ->Função que formata um número em forma monetária de acordo com a unidade monetário (dolár por padrão).
    :param f: float que representa o número a ser formatado em forma monetária
    :param m: string referente a unidade monetária, por padrão é a string 'US$'
    :return: string que representa o número formatado em forma monetária
    """
    return f'{m}{f:.2f}'.replace('.', ',')


def resumo(f=0.0, a=0.0, d=0.0, unidade='US$'):
    """
    ->Função que fornece aumentos e diminuições de um valor monetário, em forma tabular.
    :param f: float que representa o valor a ser acrescido ou descrescido
    :param a: float que representa a taxa de aumento porcentual
    :param d: float que representa a taxa de diminuição porcentual
    :param unidade: string referente a unidade monetária a ser usada na formatação dos resultados
    :return: Não possuí retorno
    """
    titulo = (print('-'*35), print('Análise do Preço'.center(35)), print('-'*35))
    analise = (print(f'Preço analisado: \t{moeda(f, unidade)}'), print(f'Dobro do preço: \t{dobro(f, True, unidade)}'),
               print(f'Metade do preço: \t{metade(f, True, unidade)}'), print(f'Aumento de {a}%: \t{aumentar(f, a, True, unidade)}'),
               print(f'Diminuição de {d}%:  {diminuir(f, d, True, unidade)}'))
    print('-'*35)


def leia_dinheiro(d):
    """
    ->Função que valida ("por cima", é uma validação incompleta) e amarzena a entrada de valores monetários.
    :param d: string, que representa o float a ser convertido
    :return: float, que representa a quantia monetária inserida
    """
    x = input(d)
    while x.isalpha() or x.isspace() or x == '':
        print('\033[0:31mPreço inválido, digite novamente.\033[m')
        x = input(d)
    return float(x.replace(',', '.'))


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


def leia_float(m='Digite um número real: '):
    """
    ->Função que lê um número real se, e somente se, a string digitada pode ser convertida no tipo primitivo float.
      No caso de não ser possível essa conversão, é printado uma string informando que o valor é inválido.
      Se a execução for interrompida, retorna o inteiro 0.
      Observação: Aceita o uso de vírgula para escrever o ponto flutuante.
    :param m: string, que se espera ser uma mensagem solicitando qual o número real em questão
    :return: float convertido da string, se possível a conversão
    """
    while True:
        try:
            x = float(input(m).replace(',', '.'))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__} Ops! O valor digitado não é um número real. Favor digite novamente.\033[m')
        except KeyboardInterrupt as erro:
            print(f'\n\033[0:31m{erro.__class__} O usuário interrompeu a execução.\033[m')
            return 0
        else:
            return x


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
    :param lista: uma lista (array), onde cada entrada dele é um item do menu
    :return: string, que corresponde a uma solicitação de qual opção (item do menu) o usuário deseja selecionar
    """
    cabecalho('MENU PRINCIPAL')
    for i, item in enumerate(lista):
        print(f'{i} - {item}')
    opc = leia_int('Sua opção: ')
    return opc
