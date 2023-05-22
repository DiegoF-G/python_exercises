print('\033[1:33mFinanciamento Imobiliário\033[m')
c = float(input('Qual o valor da casa: R$ '))
t = float(input('Em quantos anos você pretende pagar (no máximo por 20 anos): '))
s = float(input('Qual o seu salário: R$ '))
p = (c / (t*12))*1.1 # juros de 10% (1.1)
if p < 0.3*s:
    print(f'Seu empréstimo foi \033[1maprovado!\033[m O valor da prestação mensal é de R${p:.2f}')
else:
    print('Seu empréstimo \033[1mnão\033[m foi aprovado.')
# Para o empréstimo ser aprovado é necessário o valor da parcela ficar inferior a 30% do salário


