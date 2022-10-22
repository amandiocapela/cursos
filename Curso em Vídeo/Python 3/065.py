cont = maior = menor = soma = 0
seguir = 'S'

while seguir != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    seguir = input('Quer continuar? [S/N] ').strip().upper()[0]

media = soma / cont
print(f'''Você digitou {cont} números e a média foi {media}.
O maior valor foi {maior} e o menor foi {menor}''')
