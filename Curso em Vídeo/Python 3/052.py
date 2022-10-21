n = int(input('Digite um número inteiro: '))

cont = 0
for c in range(n,0,-1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}\033[m', end=' >>> ')

if cont == 2:
    print(f'\nO número {n} foi dividido por {cont} números, então ele é primo!')
else:
    print(f'\nO número {n} foi dividido por {cont} números, então ele não é primo!')