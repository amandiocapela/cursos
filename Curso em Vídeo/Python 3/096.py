def area(larg, alt):
    r = larg * alt
    print(f'A área de um terreno {larg} x {alt} é de {r} m².')


print('Controle de Terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
area(largura, altura)
