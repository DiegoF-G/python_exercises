from meu_pacote_py import modulo_ex113 as Ex113
arq = 'cursoemvideo.txt'
if not Ex113.arquivo_existe(arq):
    Ex113.criar_arquivo(arq)
while True:
    resposta = Ex113.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        Ex113.cabecalho('Pessoas Cadastradas')
        Ex113.ler_arquivo(arq)
    elif resposta == 2:
        Ex113.cabecalho('Novo Cadastro')
        nome = Ex113.formatar_nome(input('Nome: '))
        idade = Ex113.leia_int('Idade: ')
        Ex113.cadastrar(arq, nome, idade)
    elif resposta == 3:
        Ex113.cabecalho('Saindo do sistema...Até logo!')
        break
    else:
        Ex113.cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')



