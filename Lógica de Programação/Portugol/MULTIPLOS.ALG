Algoritmo "multiplos"


Var

    n1, n2, a, b : inteiro

Inicio

    escreval("Digite dois n�meros inteiros:")
    leia(n1)
    leia(n2)

    se (n1 % n2 = 0) ou (n2 % n1 = 0) ent�o
        escreval("S�o multiplos")
    senao
        escreval("N�o s�o multiplos")
    fimse

Fimalgoritmo
