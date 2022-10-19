n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

# Verificando o maior
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior!')
elif n2 > n3:
    print(f'O número {n2} é o maior!')
else:
    print(f'O número {n3} é o maior!')

# Verificando o menor
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor!')
elif n2 < n3:
    print(f'O número {n2} é o menor!')
else:
    print(f'O número {n3} é o menor!')