lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    r = input('Quer continuar? [S/N]' ).strip().upper()[0]
    if r == 'N':
        break
lista.reverse()
# lista.sort(reverse=True)

print(f'Foram digitados {len(lista)} números')
print(f'A lista de valores em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi digitado')


