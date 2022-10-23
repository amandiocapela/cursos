print('-' * 34)
print(' ' * 8, 'LOJA SUPER BARATÃO')
print('-' * 34)

total = contMaisMil = maisBaratoPreco = cont = 0
maisBaratoProduto = ''
while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço R$:'))
    cont += 1
    total += preco
    if preco > 1000:
        contMaisMil += 1
    if cont == 1 or preco < maisBaratoPreco:
        maisBaratoPreco = preco
        maisBaratoProduto = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {contMaisMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {maisBaratoProduto} que custa R${maisBaratoPreco:.2f}')

