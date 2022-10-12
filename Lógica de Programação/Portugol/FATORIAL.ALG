Algoritmo "fatorial"

Var

   n, i, fat : inteiro

Inicio

   fat <- 1
   escreva("Digite o valor de N: ")
   leia(n)
   
   para i de n ate 1 passo -1 faca
      fat <- i * fat
   fimpara
   escreval("Fatorial = ", fat)

Fimalgoritmo