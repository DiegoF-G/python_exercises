def fatorial(n, show=False):
    """
    ->Cálculo do fatorial de um número inteiro nao negativo, definindo para 0 a imagem 1 (0! = 1).
    :param n: inteiro que vai ser calculado seu respectivo fatorial
    :param show: booleano que determina se é mostrado ou não detalhes do calculo do fatorial
    :return: inteiro que é o fatorial de n, uma string que mostra os detalhes do cálculo do fatorial de n ou mensagem
    de parametro inválido para o cálculo do fatorial
    """
    if n >= 0:
        num = n
        f = f'{n}'
        if n != 0:
            for i in range(n - 1, 0, -1):
                f += f'*{i}'
                n *= i
            if show:
                return f'{num}! = {f} = {n}'
            else:
                return n
        else:
            if show:
                return f'{n}! = 1'
            else:
                return 1
    else:
        return '\033[0:31mparametro inválido, fatorial só está definido para inteiros não negativos.\033[m'


testes = (print(fatorial(0, True)), print(fatorial(0)), print(fatorial(3, show=True)), print(fatorial(5)),
          print(fatorial(-5)), help(fatorial))


# def fatorial(n, show=False):
#     from math import factorial
#     f = f'{n}'
#     for i in range(n - 1, 0, -1):
#         f += f'*{i}'
#     if n != 0:
#         if show:
#             return f'{n}! = {f} = {factorial(n)}'
#         else:
#             return factorial(n)
#     else:
#         if show:
#             return '0! = 1'
#         else:
#             return 1








