print('=' * 30)
print('{:^30}'.format('BANCO ADCN'))
print('=' * 30)

# Opção 1:
'''sacar = int(input('Que valor você quer sacar? R$'))

while sacar != 0:
    n50 = sacar // 50
    sacar = sacar % 50
    if n50 != 0:
        print(f'Total de {n50} notas de R$50')
    n20 = sacar // 20
    sacar = sacar % 20
    if n20 != 0:
        print(f'Total de {n20} notas de R$20')
    n10 = sacar // 10
    sacar = sacar % 10
    if n10 != 0:
        print(f'Total de {n10} notas de R$10')
    n1 = sacar // 1
    sacar = sacar % 1
    if n1 != 0:
        print(f'Total de {n1} notas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO ADCN. Tenha um bom dia!')
'''
# Opção 2:
sacar = int(input('Que valor você quer sacar? R$'))
total = sacar
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO ADCN. Tenha um bom dia!')

