Algoritmo "numeros_pares"

Var

    n, i, cont : inteiro

    vet : vetor [0..99] de inteiro

Inicio

    escreva("Quantos n�meros voc� vai digitar?")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreva("Digite um n�mero: ")
        leia(vet[i])
    fimpara
    
    cont <- 0
    
    para i de 0 ate n-1 faca
        se vet[i] % 2 = 0 entao
            cont <- cont + 1
        fimse
    fimpara
    
    escreval
    escreval("N�meros Pares:")
    
    para i de 0 ate n-1 faca
        se vet[i] % 2 = 0 entao
            escreva(vet[i], " ")
        fimse
    fimpara
    
    escreval
    escreval("Quantidade de Pares = ", cont)

Fimalgoritmo