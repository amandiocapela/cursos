vel = eval(input('Qual a velocidade do carro? '))

multa = 0
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado em R${multa:.2f}!')
else:
    print('Você não foi multado.')
