from meu_pacote_py import modulo_ex113 as ex113
arq = 'cursoemvideo.txt'
if not ex113.arquivo_existe(arq):
    ex113.criar_arquivo(arq)
while True:
    resposta = ex113.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ex113.cabecalho('Pessoas Cadastradas')
        ex113.ler_arquivo(arq)
    elif resposta == 2:
        ex113.cabecalho('Novo Cadastro')
        nome = ex113.formatar_nome(input('Nome: '))
        idade = ex113.leia_int('Idade: ')
        ex113.cadastrar(arq, nome, idade)
    elif resposta == 3:
        ex113.cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        ex113.cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
