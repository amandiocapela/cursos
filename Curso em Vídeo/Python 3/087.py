matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna = maiorLinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

for l in range(0, 3):
    somaColuna += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maiorLinha = matriz[1][c]
    elif matriz[1][c] > maiorLinha:
        maiorLinha = matriz[1][c]

print('-=' * 30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaColuna}.')
print(f'O maior valor da segudna linha é {maiorLinha}.')
