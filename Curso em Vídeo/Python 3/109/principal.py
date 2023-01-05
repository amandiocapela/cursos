import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {(moedas.metade(p, True))}')
print(f'O dobro de {moedas.moeda(p)} é {(moedas.dobro(p, True))}')
print(f'Aumentando 10% em {moedas.moeda(p)}, temos {(moedas.aumentar(p, 10, True))}')
print(f'Diminuindo 10% em {moedas.moeda(p)}, temos {(moedas.diminuir(p, 10, True))}')
