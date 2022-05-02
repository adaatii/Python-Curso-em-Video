from d115.lib1.interface import *
from d115.lib1.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de Listar o conteúdo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = leiaStr('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção sair do sistema.
        cabecalho('Saindo do sistema... Até logo.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
