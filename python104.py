def panorama(*n, sit=False):
    """
    ->Função que pega notas (aceita um número arbritário delas) e determina quantas foram, a maior, a menor e a média,
      além de mostrar a situação como opcional.
    :param n: tupla de floats, que são as notas
    :param sit: booleano, opcional, que determina se é mostrado ou não a situação
    :return: se a tupla for vazia retorna uma string informando que nenhuma nota foi digitada, se a tupla for não vazia
             retorna um dicionário com todas informações sobre as notas
    """
    if len(n) > 0:
        pan = dict()
        pan['Total'] = len(n)
        pan['Maior'] = max(n)
        pan['Menor'] = min(n)
        m = pan['Média'] = sum(n) / len(n)
        if sit:
            if m >= 7:
                pan['Situação'] = 'ÓTIMO'
            elif 5 <= m < 7:
                pan['Situação'] = 'BOM'
            elif m < 5:
                pan['Situação'] = 'RUIM'
        return pan
    else:
        return 'Nenhuma nota digitada.'


testes = (print(panorama()), print(), print(panorama(1, 2, 5, 10)), print(), print(panorama(5, 5.2, sit=True)), print(),
          print(panorama(10, sit=True)), print(), print(panorama(10, 0, 5.5, sit=True)), print(),
          print(panorama(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sit=True)), print(), print(panorama(sit=True)), print(),
          print(panorama(5, 3, sit=True)), help(panorama))
