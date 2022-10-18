n = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
valorDia = n * 60
valorKm = km * 0.15
pagar = valorDia + valorKm

print(f'O total a pagar é de R${pagar:.2f}')
