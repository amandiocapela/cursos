N = int(input("Quantos números você vai digitar? "))

vet = [0 for x in range(N)]


for i in range(0, N):
    vet[i] = int(input("Digite um número: "))

print()
print(f"Valores = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f} ", end="")
print()

soma = 0
for i in range(0,N):
    soma += vet[i]

print(f"Soma = {soma:.2f}")
media = soma / N
print(f"Média = {media:.2f}")
