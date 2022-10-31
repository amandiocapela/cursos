lista = []
for v in range(0, 5):
    lista.append(int(input('Digite um número: ')))

maior = max(lista)
menor = min(lista)
print('=-' * 30)
print(f'A lista digitada foi {lista}')
print(f'O maior valor digitado foi {maior} e ele está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} e ele está nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()

