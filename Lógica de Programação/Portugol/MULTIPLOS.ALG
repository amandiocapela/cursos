Algoritmo "multiplos"


Var

    n1, n2, a, b : inteiro

Inicio

    escreval("Digite dois números inteiros:")
    leia(n1)
    leia(n2)

    se (n1 % n2 = 0) ou (n2 % n1 = 0) então
        escreval("São multiplos")
    senao
        escreval("Náo são multiplos")
    fimse

Fimalgoritmo
