Algoritmo "maior_posicao"


Var

   n, i, posicao : inteiro
   maior : real
   vet : vetor [0..99] de real

Inicio

    escreva("Quantos números você vai digitar? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreva("Digite um número: ")
        leia(vet[i])
    fimpara
    
    maior <- vet[0]
    posicao <- 0
    
    para i de 0 ate n-1 faca
        se vet[i] > maior entao
        maior <- vet[i]
        posicao <- i
        fimse
     fimpara
     
     escreval
     escreval("Maior Valor = ", maior:1:2)
     escreval("Posição do maior valor = ", posicao)


Fimalgoritmo