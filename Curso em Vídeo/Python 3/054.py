from datetime import datetime

hoje = datetime.today().year
maior = 0
menor = 0
for c in range(1,8):
    n = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if hoje - n >= 18:
        maior += 1
    else:
        menor += 1
        
print()
print(f'''Ao todo tivemos {maior} pessoas maiores de idade
E também tivemos {menor} pessoas menores de idade.''')