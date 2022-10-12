Algoritmo "lanchonete"

Var

    cod, qtd : inteiro
    valor, total : real

Inicio




    escreva("Código do produto comprado: ")
    leia(cod)
    escreva("Quantidade comprada: ")
    leia(qtd)

    escolha cod
        caso 1
            valor <- 5.00
        caso 2
            valor <- 3.50
        caso 3
            valor <- 4.80
        caso 4
            valor <- 8.90
        caso 5
            valor <- 7.32
        fimescolha

    total <- qtd * valor
    
    escreval("Valor a pagar: ", total:1:2)
    
    
Fimalgoritmo