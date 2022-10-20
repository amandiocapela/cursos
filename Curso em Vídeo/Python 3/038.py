n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O primeiro número é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')