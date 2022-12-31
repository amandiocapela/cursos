from random import randint
from time import sleep


def sortear():
    cont = 0
    print(f'Sorteando 5 valores entre 0 e 10: ', end='')
    while cont < 5:
        a = randint(0, 10)
        sorteados.append(a)
        print(f'{sorteados[cont]}', end=' ')
        cont += 1
        sleep(0.25)
    print('PRONTO!')


def somarpar():
    somapares = 0
    for c in range(0, 5):
        if sorteados[c] % 2 == 0:
            somapares += sorteados[c]
    print(f'Somando os valores pares de {sorteados}, temos {somapares}')


# Programa Principal
sorteados = []
sortear()
somarpar()
