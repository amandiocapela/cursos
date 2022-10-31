pessoas = []
dados = []
maiorPeso = menorPeso = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = input('Quer continuar? [S/N]: ')
    if r in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)}.')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=' ')
print()
print(f'O menor peso foi de {menorPeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=' ')
print()
