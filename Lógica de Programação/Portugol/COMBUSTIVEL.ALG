Algoritmo "combustivel"


Var

    n, alcool, gasolina, diesel : inteiro
    

Inicio

   alcool <- 0
   gasolina <- 0
   diesel <- 0
   
   escreva("Informe um código (1, 2, 3) ou 4 para parar: ")
   leia(n)
   
   enquanto n <> 4 faca
   
       escolha n
       caso 1
           alcool <- alcool + 1
       caso 2
           gasolina <- gasolina + 1
       caso 3
           diesel <- diesel + 1
       fimescolha

       escreva("Informe um código (1, 2, 3) ou 4 para parar: ")
       leia(n)
    fimenquanto
    
    escreval("Muito Obrigado")
    escreval("Alcool: ", alcool)
    escreval("Gasolina: ", gasolina)
    escreval("Diesel: ", diesel)


Fimalgoritmo