def voto(b):
    '''
    A função voto() retorna sobre a obrigação de voto de um cidadão de acordo com as leis eleitorais em 2023 no Brasil.
    :param b: Ano de nascimento do cidadão
    :return: As strings: 'Voto NEGADO.', 'Voto OPCIONAL.' ou 'Voto OBRIGATÓRIO.'
    '''
    from datetime import date
    y = date.today().year - b
    if 0 <= y < 16:
        return 'Voto NEGADO.'
    elif 0 < 16 <= y <= 17 or y >= 60:
        return 'Voto OPCIONAL.'
    elif y >= 18:
        return 'Voto OBRIGATÓRIO.'
    else:
        return f'\033[0:31mDado Inválido.\033[m'


anoNascimento = int(input('Digite o ano de nascimento: '))
print(voto(anoNascimento))














