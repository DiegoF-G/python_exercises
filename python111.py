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


testes = (print(leia_int()), print(leia_float()))
