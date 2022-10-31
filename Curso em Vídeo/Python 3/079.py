list = []
continuar = ''
while True:
    n = int(input('Digite um valor: '))
    if n in list:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        list.append(n)
        print('Valor adicionado com sucesso...')
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
list.sort()
print('-=' * 30)
print(f'Você digitou os valores {list}')
