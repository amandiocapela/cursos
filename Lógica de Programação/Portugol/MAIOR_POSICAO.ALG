Algoritmo "maior_posicao"


Var

   n, i, posicao : inteiro
   maior : real
   vet : vetor [0..99] de real

Inicio

    escreva("Quantos n�meros voc� vai digitar? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreva("Digite um n�mero: ")
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
     escreval("Posi��o do maior valor = ", posicao)


Fimalgoritmo