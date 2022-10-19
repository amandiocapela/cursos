sal = float(input('Qual o salário a ser analisado? '))

salNovo = 0

if sal >= 1250:
    salNovo = sal * 1.1
else:
    salNovo = sal * 1.15

print(f'O novo salário será R${salNovo:.2f}')