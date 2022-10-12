Algoritmo "dados_pessoas"


Var

    n, i, contF, contM, homens : inteiro

    menor, maior, soma, media : real

    altura : vetor [0..99] de real
    genero : vetor [0..99] de caractere
    
Inicio

    escreva("Quantas pessoas serão digitadas? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreva("Altura da ", i+1, "a pessoa: ")
        leia(altura[i])
        escreva("Gênero da ", i+1, "a pessoa: ")
        leia(genero[i])
    fimpara
    
    menor <- altura[0]
    maior <- altura[0]
    
    para i de 0 ate n-1 faca
        se altura[i] < menor entao
            menor <- altura[i]
        fimse
        se altura[i] > maior entao
            maior <- altura[i]
        fimse
    fimpara
    
    escreval("Menor altura = ", menor:3:2)
    escreval("Maior altura = ", maior:3:2)
    
    media <- 0
    contF <- 0
    
    para i de 0 ate n-1 faca
        se genero[i] = "F" entao
            soma <- soma + altura[i]
            contF <- contF + 1
        fimse
    fimpara
    
    media <- soma / contF
    
    escreval("Média das alturas das mulheres = ", media:4:2)
    
    contM <- n - contF
    
    escreval("Número de homens = ", contM)

Fimalgoritmo