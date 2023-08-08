def informar_maior(*x):
    if len(x) == 0:
        print('Nenhum número informado, não existe maior.')
    elif len(x) == 1:
        print(f'Apenas 1 número informado, {x[0]}, o maior é ele mesmo.')
    else:
        print(f'Dos {len(x)} números informados o maior é {max(x)}.'),
        print(f'Números informados: {str(x).replace("(", "").replace(")", "")}')


testes = (informar_maior(1, 2, 3, 5.5, 0.2), print(), informar_maior(0), print(),
          informar_maior(2, 22, 222, 222.001, 222.0005, 0), print(), informar_maior())
