def ajuda(msg):
    help(msg)


def cabecalho(cab):
    tam = len(cab.strip()) + 4
    print('~' * tam)
    print(f'  {cab}')
    print('~' * tam)


while True:
    cabecalho('Sistema de Ajuda PyHelp')
    r = input('Função ou Biblioteca > ').strip().lower()
    if r != 'sair':
        cabecalho(r)
        ajuda(r)
    else:
        break
