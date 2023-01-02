from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: Não Vota!')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos: Voto Opcional!')
    elif 18 <= idade < 60:
        print(f'Com {idade} anos: Voto Obrigatório!')
    else:
        print(f'Com {idade} anos: Voto Opcional!')


voto(int(input('Em que ano você nasceu? ')))
