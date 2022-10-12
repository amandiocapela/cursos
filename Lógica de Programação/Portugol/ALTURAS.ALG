Algoritmo "alturas"


Var

    n, i, qtd : inteiro
    somaAltura, mediaAltura, percIdade : real

    vetNome : vetor [0..9] de caractere
    vetIdade : vetor [0..9] de inteiro
    vetAltura : vetor [0..9] de real

Inicio

    escreva("Quantas pessoas serão digitadas?")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreval("Dados da ", i+1, "a pessoa: ")
        escreva("Nome: ")
        leia(vetNome[i])
        escreva("Idade: ")
        leia(vetIdade[i])
        escreva("Altura: ")
        leia(vetAltura[i])
    fimpara
    
    somaAltura <- 0
    
    para i de 0 ate n-1 faca
        somaAltura <- somaAltura + vetAltura[i]
    fimpara
    
    mediaAltura <- somaAltura / n
    
    escreval
    escreval("Altura média: ", mediaAltura:1:2)
    
    qtd <- 0
    
    para i de 0 ate n-1 faca
        se vetIdade[i] < 16 entao
            qtd <- qtd + 1
        fimse
    fimpara
    
    percIdade <- qtd / n * 100
    
    escreval("Pessoas com menos de 16 anos: ", percIdade:1:1, "%")
    
    para i de 0 ate n-1 faca
        se vetIdade[i] < 16 entao
            escreval(vetNome[i])
        fimse
    fimpara
    
Fimalgoritmo