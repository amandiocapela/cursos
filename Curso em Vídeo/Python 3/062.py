primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

cont = 1
termo = primeiro
qtd = 10
termos = 0
while qtd != 0:
    while cont <= qtd:
        print(termo, end=' >>> ')
        cont += 1
        termos += 1
        termo += razao
    print('PAUSA')
    cont = 1
    qtd = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {termos} mostrados')