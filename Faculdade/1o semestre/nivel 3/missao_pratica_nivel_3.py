# Cécula 1
# Função para solicitar ao usuário e criar seu conjunto
def qualConjunto():
    global Q
    Q = int(input("Quantos elementos seu conjunto terá? "))
    for elemento in range(0, Q):
        conjunto.append(input("Escreva um elemento: "))
    return conjunto

# Cécula 2
# Criar 1ª parte Subconjunto
def subConj1(subConj):
    return subConj2([],subConj)

# Criar 2ª parte Subconjunto e finalizar
def subConj2(current, conj):
    if conj:
        return subConj2(current,conj[1:]) + subConj2(current+[conj[0]],conj[1:])
    return [current]

# Célula 3
# Início do Programa
conjunto = []
conj = conjunto
qualConjunto()

print(f"O conjunto digitado pelo usuário foi: {conjunto}")

# Quantidade de Subconjuntos
qtdSubConj = 2**Q
print(f"A quantidade de subconjuntos é: {qtdSubConj}")

print(f"Os subconjuntos são: {sorted(subConj1(conj))}")
