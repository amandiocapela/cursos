L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
area = L * A
litroTinta = area / 2

print(f'Sua parece tem a dimensão de {L} x {A} e sua área é de {area}')
print(f'Para pintar essa parede, você precisará de {litroTinta}l de tinta.')
