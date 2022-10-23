from random import randint

print('=-=' * 10)
print('Vamos jogar PAR ou ÍMPAR!')
print('=-=' * 10)

vencidas = 0
while True:
    nComputador = randint(1, 5)
    jogador = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    nJogador = int(input('Digite um valor: '))
    total = nJogador + nComputador
    if total % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    if jogador != pi.replace('Í', 'I')[0]:
        print('-' * 30)
        print(f'Você jogou {nJogador} e o computador {nComputador}. Total de {total} deu {pi}.')
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {vencidas} vezes')
        print('-' * 30)
        break
    else:
        vencidas += 1
        print('-' * 30)
        print(f'Você jogou {nJogador} e o computador {nComputador}. Total de {total} deu {pi}.')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-' * 30)