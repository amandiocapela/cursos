import interface
import arquivo
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver Pessoas Cadastras', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        interface.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt(input('Idade: '))
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
