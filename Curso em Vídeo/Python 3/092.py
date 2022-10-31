from datetime import datetime
trabalhador = {}

trabalhador['nome'] = input('Nome: ')
trabalhador['idade'] = datetime.today().year - int(input('Ano de Nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] > 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.today().year)

print('-=-' * 30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')

