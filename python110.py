import meuPacotePy.dado as dado
import meuPacotePy.moeda as moeda
dinheiro = dado.leia_dinheiro('Digite um preço em reais: R$ ')
moeda.resumo(dinheiro, 10, 10, 'R$')


