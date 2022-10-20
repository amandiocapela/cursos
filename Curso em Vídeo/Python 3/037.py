n = int(input('Digite um número inteiro: '))

print('''Escolha em qual base deseja converter:
[ 1 ] Base Binária
[ 2 ] Base Octal
[ 3 ] Base Hexadecimal''')

b = int(input('Digite o número da sua opção: '))

if b == 1:
    print(f'{n} convertido em Binário é igual a {bin(n)[2:]}')
elif b == 2:
    print(f'{n} convertido em Octal é igual a {oct(n)[2:]}')
elif b == 3:
    print(f'{n} convertido em Hexadecimal é igual a {hex(n)[2:]}')
else:
    print(f'Opção {n} não é válida.')
