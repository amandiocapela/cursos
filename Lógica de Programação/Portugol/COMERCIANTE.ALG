Algoritmo "comerciante"


Var

   n, i, cont1, cont2, cont3 : inteiro
   
   totalCompra, totalVenda, lucro, lucroTotal, percentualLucro : real
   
   nome : vetor [0..99] de caractere
   compra : vetor [0..99] de real
   venda : vetor [0..99] de real
    
Inicio

    escreva("Serão digitados dados de quantos produtos? ")
    leia(n)
    
    para i de 0 ate n-1 faca
        escreval("Produto ", i+1, ":")
        escreva("Nome: ")
        leia(nome[i])
        escreva("Preço de Compra: ")
        leia(compra[i])
        escreva("Preço de Venda: ")
        leia(venda[i])
    fimpara
    

    cont1 <- 0
    cont2 <- 0
    cont3 <- 0
    para i de 0 ate n-1 faca
        lucro <- venda[i] - compra[i]
        percentualLucro <- lucro * 100 / compra[i]
        se percentualLucro < 10 entao
            cont1 <- cont1 + 1
        senao
            se percentualLucro <= 20 entao
                cont2 <- cont2 + 1
                senao
                    cont3 <- cont3 + 1
            fimse
        fimse
    fimpara
    
    totalCompra <- 0
    totalVenda  <- 0
    
    para i de 0 ate n-1 faca
         totalCompra <- totalCompra + compra[i]
         totalVenda <- totalVenda + venda[i]
    fimpara
    
    lucroTotal <- totalVenda - totalCompra
    
    escreval
    escreval("Relatório:")
    escreval("Lucro abaixo de 10%: ", cont1)
    escreval("Lucro entre 10% e 20%: ", cont2)
    escreval("Lucro acima de 20%: ", cont3)
    escreval("Valor total de compra: ", totalCompra:4:2)
    escreval("Valor total de Venda: ", totalVenda:4:2)
    escreval("Lucro Total: ", lucroTotal:4:2)

Fimalgoritmo