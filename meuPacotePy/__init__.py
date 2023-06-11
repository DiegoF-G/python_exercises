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
    :param m: string, que se espera ser uma mensagem solicitando qual o inteiro em questão
    :return: inteiro, convertido da string se possível a conversão
    """
    while True:
        try:
            n = int(input(m))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__}. Ops! O valor digitado não é um inteiro. Favor digite novamente.\033[m')
        else:
            return n


def leia_float(m='Digite um número real: '):
    """
    ->Função que lê um número real se, e somente se, a string digitada pode ser convertida no tipo primitivo float.
      No caso de não ser possível essa conversão, é printado uma string informando que o valor é inválido.
      Observação: Aceita o uso de vírgula para escrever o ponto flutuante.
    :param m: string, que se espera ser uma mensagem solicitando qual o número real em questão
    :return: float convertido da string, se possível a conversão
    """
    while True:
        try:
            x = float(input(m).replace(',', '.'))
        except Exception as erro:
            print(f'\033[0:31m{erro.__class__}. Ops! O valor digitado não é um número real. Favor digite novamente.\033[m')
        else:
            return x


