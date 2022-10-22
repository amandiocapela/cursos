from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

# Opção 1:
n = randint(0, 10)
palpite = int(input('Qual é seu palpite? '))
tentativas = 1

while palpite != n:
    tentativas += 1
    if n > palpite:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual é seu palpite? '))

print(f'Acertor com {tentativas} tentativas. Parabéns!')

# Opção 2:
'''n = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite == n:
        acertou = True
    else:
        if n > palpite:
            print('Mais... Tente mais uma vez.')
        elif n < palpite:
            print('Menos... Tente mais uma vez.')
print(f'Acertor com {tentativas} tentativas. Parabéns!')'''



