Algoritmo "pares_consecutivos"


Var

    x, count, soma : inteiro

Inicio

    count <- 0
    soma <- 0
    
    escreva("Digite um número inteiro: ")
    leia (x)


    enquanto x <> 0 faca
        enquanto (count < 5) faca
            se x % 2 = 0 entao
                soma <- soma + x
                count <- count + 1
            fimse
            x <- x + 1
        fimenquanto
    escreval("Soma = ", soma)
    count <- 0
    soma <- 0
    escreva("Digite um número inteiro: ")
    leia (x)
    fimenquanto


Fimalgoritmo