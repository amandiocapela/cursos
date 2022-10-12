print("Digite dois números:")
a = int(input())
b = int(input())

if a > b:
   troca = a
   a = b
   b = troca

soma = 0
for i in range(a+1, b):
    if i % 2 != 0:
        soma += i

print(f"Soma dos Ímpares: {soma}")