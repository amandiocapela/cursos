from random import randrange

computador = randrange(1, 4)
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Digite o número da sua opção: '))

if computador == 1:
    if jogador == 1:
        print(f'O Computador escolheu PEDRA e vocês empataram!')
    elif jogador == 2:
        print(f'O Computador escolheu PEDRA e você ganhou!')
    elif jogador == 3:
        print(f'O Computador escolheu PEDRA e você perdeu!')
    else:
        print(f'{jogador} não é uma opção válida.')
elif computador == 2:
    if jogador == 1:
        print(f'O Computador escolheu PAPEL e você perdeu!')
    elif jogador == 2:
        print(f'O Computador escolheu PAPEL e voces empataram!')
    elif jogador == 3:
        print(f'O Computador escolheu PAPEL e você ganhou!')
    else:
        print(f'{jogador} não é uma opção válida.')
elif computador == 3:
    if jogador == 1:
        print(f'O Computador escolheu TESOURA e você ganhou!')
    elif jogador == 2:
        print(f'O Computador escolheu TESOURA e voce perdeu!')
    elif jogador == 3:
        print(f'O Computador escolheu TESOURA e vocês empataram!')
    else:
        print(f'{jogador} não é uma opção válida.')
