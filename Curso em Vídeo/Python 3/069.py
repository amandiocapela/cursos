print('-' * 10)
print('CADASTRE UMA PESSOA')
print('-' * 10)

contMais18 = 0
contHomens = 0
contMulheresMenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('-' * 10)
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if idade >= 18:
        contMais18 += 1
    if sexo == 'M':
        contHomens +=1
    if sexo == 'F' and idade <= 20:
        contMulheresMenos20 += 1
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {contMais18}
Ao todo temos {contHomens} homens cadastrados
E temos {contMulheresMenos20} com menos de 20 anos.''')
