n = eval(input("Digite um número\n"))

nresto = str(n % 2)
nint = n // 2
numero_base_binaria = list

while nint != 0:
    nresto = nresto + str(nint % 2)
    nint = nint // 2

numero_base_binaria = nresto
numero_base_binaria = int(numero_base_binaria[::-1])

print(f'Número na base decimal = {n}')
print(f'Conversão para base binária = {numero_base_binaria}')