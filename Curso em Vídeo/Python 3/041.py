from datetime import datetime
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = datetime.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria JUNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')