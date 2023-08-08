import meu_pacote_py.dado as dado
import meu_pacote_py.moeda as moeda
dinheiro = dado.leia_dinheiro('Digite um preço em reais: R$ ')
moeda.resumo(dinheiro, 10, 10, 'R$')
