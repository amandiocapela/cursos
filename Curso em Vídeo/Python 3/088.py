from random import randint
from time import sleep

print('-' * 50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-' * 50)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {jogos} JOGOS', '=-' * 3)

lista = []
jogo = []

for c in range(0, jogos):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
for i, l in enumerate(lista):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 3, '< Boa Sorte! >', '=-' * 3)


