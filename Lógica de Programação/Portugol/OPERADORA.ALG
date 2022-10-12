Algoritmo "operadora"

Var

   min : inteiro
   valor : real

Inicio

   escreva("Digite a quantidade de minutos: ")
   leia(min)
   
   valor <- 50.00
   
   se min > 100 então
      valor <- valor + (2 * (min - 100))
   fimse
   
   escreval("Valor a pagar: R$", valor:1:2)

Fimalgoritmo