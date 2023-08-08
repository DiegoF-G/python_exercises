""" A precisão dos floats em comparação com números em base 10 muitas vezes podem ser satisfatórias e muitas vezes não.
    No caso de ser necessário um "float exato", existe o módulo "decimal" que traz o tipo Decimal, que pega o float
    e o transforma num número base 10 de fato."""
from decimal import Decimal
ganhos_julho_base2 = 99.91*5
ganhos_julho_decimal = Decimal('99.91') * 5
diferencaGanhos = (print(ganhos_julho_base2), print(ganhos_julho_decimal), print(float(ganhos_julho_decimal)-ganhos_julho_base2))
print()
gastos_julho_base2 = 110.1*3
gastos_julho_decimal = Decimal('110.1') * 3
diferencaGastos = (print(gastos_julho_base2), print(gastos_julho_decimal), print(float(gastos_julho_decimal)-gastos_julho_base2))
