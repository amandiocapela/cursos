from random import randint

n = randint(1, 5)

u = int(input('Adivinhe o número: '))

if u == n:
    print('Acertou! Parabéns!')
else:
    print(f'Errou! Eu pensei no número {n}!')