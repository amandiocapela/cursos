from datetime import datetime

ano = int(input('Digite seu ano de nascimento: '))
alist = ano + 18
atual = datetime.today().year
dif = alist - atual

if dif > 0:
    print(f'Você ainda deve se alistar no serviço militar. Faltam {dif} anos.')
elif dif < 0:
    print(f'Você deveria ter se alisatado há {-dif} anos.')
else:
    print('Você deve se alistar neste ano!')
