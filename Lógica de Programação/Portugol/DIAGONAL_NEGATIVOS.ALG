Algoritmo "diagonal_negativos"

Var

    N, i, j, contNeg : inteiro
    mat : vetor [0..9, 0..9] de inteiro

Inicio

   escreva("Qual a ordem da matriz? ")
   leia(N)
   
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
          escreva("Elemento [", i,",", j, "]: ")
          leia(mat[i,j])
      fimpara
   fimpara
   
   escreval("Diagonal Principal:")
   
   para i de 0 até N-1 faca
      escreva(mat[i,i], " ")
   fimpara
   escreval
   
   contNeg <- 0
   
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
          se mat[i,j] < 0 entao
             contNeg <- contNeg + 1
          fimse
      fimpara
   fimpara
   
   escreval("Quantidade de Negativos: ", contNeg)

Fimalgoritmo