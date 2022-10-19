dist = float(input('Qual a distância da sua viagem? '))

valor = 0
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
# valor = dist * 0.50 if dist <= 200 else dist * 0.45

print(f'O valor da viagem é R${valor:.2f}')