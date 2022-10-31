lista = []
listaPares = []
listaImpares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)
    r = input('Quer continuar? [S/N]' )
    if r in 'Nn':
        break

print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPares}')
print(f'A lista de ímpares é {listaImpares}')