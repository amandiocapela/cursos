Algoritmo "soma_vetor"


Var

   n, i : inteiro
   vet : vetor [0..9] de real
   soma, media : real

Inicio

    escreva("Quantos n�meros voc� vai digitar? ")
    leia(n)
    
    soma <- 0
    
    para i de 0 ate n-1 faca
        escreva("Digite um n�mero: ")
        leia(vet[i])
        soma <- soma + vet[i]
    fimpara
    
    escreval
    escreval("Valores = ")
    para i de 0 ate n-1 faca
        escreva(vet[i]:3:1, " ")
    fimpara

    //soma <- 0
    
    //para i de 0 ate n-1 faca
    //    soma <- soma + vet[i]
    //fimpara
    
    escreval("Soma = ", soma:4:2)
    
    media <- soma / n
    
    escreval("M�dia = ", media: 4:2)
    
Fimalgoritmo