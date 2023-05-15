e = input('Escreva uma expressão matemática com parentêses e com operações aritméticas simples: ').strip()
p = []
for s in e:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')


