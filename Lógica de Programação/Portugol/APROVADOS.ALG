Algoritmo "aprovados"


Var

    n, i : inteiro
    media : real
    nome : vetor [0..99] de caractere
    nota1 : vetor [0..99] de real
    nota2 : vetor [0..99] de real
    //media : vetor [0..99] de real
    
Inicio

    escreva("Quantos alunos serão digitados? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreval("Digite o nome, primeira e segunda nota do ", i+1, "o aluno:")
        leia(nome[i])
        leia(nota1[i])
        leia(nota2[i])
    fimpara
    
    //para i de 0 ate n-1 faca
    //    media[i] <- (nota1[i] + nota2[i]) / 2
    //fimpara
    
    escreval("Alunos Aprovados:")
    para i de 0 ate n-1 faca
        media < - (nota1[i] + nota2[i]) / 2
        se media >= 6 entao
            escreval(nome[i])
        fimse
        //se media[i] >= 6.0 entao
            //escreval(nome[i])
        //fimse
    fimpara

Fimalgoritmo