from time import sleep

def contador(ini, fim, passo):
    print('-=' * 30)
    print(f'Contando de {ini} até {fim} de {passo} em {passo}')
    for c in range(ini, fim+1, passo):
        print(c, end=' ')
        sleep(0.1)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez de personalizar a contagem')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

if a < b:
    if c < 0:
        c = -c
else:
    if c > 0:
        c = -c

contador(a, b, c)







