Algoritmo "mais_velho"


Var

    n, i, idadeMaior, idMaior : inteiro
    nomeMaior: caractere

    nome : vetor [0..99] de caractere
    idade : vetor [0..99] de inteiro
    
Inicio

    escreva("Quantas pessoas você vai digitar? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreval("Dados da ", i+1, "a pessoa:")
        escreva("Nome: ")
        leia(nome[i])
        escreva("Idade: ")
        leia(idade[i])
    fimpara
    
    idadeMaior <- 0
    idMaior <- 0
    
    para i de 0 ate n-1 faca
        se idade[i] > idadeMaior entao
            idadeMaior <- idade[i]
            idMaior <- i
        fimse
    fimpara
    
    escreval("Pessoa Mais Velha: ", nome[idMaior])

Fimalgoritmo