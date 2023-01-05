import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moedas.metade(p)}')
print(f'O dobro de {p} é R${moedas.dobro(p)}')
print(f'Aumentando 10% em {p}, temos R${moedas.aumentar(p, 10)}')
