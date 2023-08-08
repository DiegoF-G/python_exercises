print('\033[4:33mSEQUÊNCIA DE FIBONACCI\033[m')
n = int(input('Até qual termo, partindo do primeiro, você deseja da Sequência de Fibonacci: '))
while n <= 0:
    n = int(input('Opção inválida! Digite novamente até qual termo você deseja da Sequência de Fibonacci: '))
if n == 1:
    print('0')
elif n == 2:
    print('0 -> 1')
elif n == 3:
    print('0 -> 1 -> 1')
elif n == 4:
    print('0 -> 1 -> 1 -> 2')
else:
    a1 = 0
    a2 = 1
    a_ante_anterior = a2 + a1  # a3
    a_anterior = a_ante_anterior + a2  # a4
    print('0 -> 1 -> 1 -> 2', end=' -> ')
    c = 0
    while c < n - 4:
        if c < n - 5:
            c += 1
            a_seguinte = a_anterior + a_ante_anterior
            print(a_seguinte, end=' -> ')
            a_ante_anterior = a_anterior
            a_anterior = a_seguinte
        else:
            c += 1
            a_seguinte = a_anterior + a_ante_anterior
            print(a_seguinte)
