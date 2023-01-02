def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


jogador = input('Nome do jogador: ')
qtd = input('Número de gols: ')
if qtd.isnumeric():
    qtd = int(qtd)
else:
    qtd = 0
if jogador.strip() == '':
    ficha(gols=qtd)
else:
    ficha(jogador, qtd)

