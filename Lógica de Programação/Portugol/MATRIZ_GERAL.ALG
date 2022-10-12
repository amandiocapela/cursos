Algoritmo "matriz_geral"

Var

   N, i, j, k : inteiro
   soma : real
   mat : vetor [0..9, 0..9] de real

Inicio

   escreva("Qual a ordem da matriz? ")
   leia(N)
   
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
         escreva("Elemento [", i, ", ", j, "]: ")
         leia(mat[i, j])
      fimpara
   fimpara
   
   soma <- 0
   
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
         se mat[i, j] > 0 entao
            soma <- soma + mat[i, j]
         fimse
      fimpara
   fimpara
   escreval
   
   escreval("Soma dos positivos: ", soma:3:1)
   escreval
   
   escreva("Escolha uma linha: ")
   leia(k)
   
   escreva("Linha Escolhida :")
   para j de 0 ate N-1 faca
      escreva(mat[k, j]:3:1, " ")
   fimpara
   escreval
   escreval

   escreva("Escolha uma coluna: ")
   leia(k)

   escreva("Coluna Escolhida :")
   para i de 0 ate N-1 faca
      escreva(mat[i, k]:3:1, " ")
   fimpara
   escreval
   escreval
   
   escreva("Diagonal Principal: ")
   para i de 0 ate N-1 faca
         escreva(mat[i, i]:2:1, " ")
   fimpara
   escreval
   escreval
   
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
         se mat[i, j] < 0 entao
            mat[i, j] <- mat[i,j]^2
         fimse
      fimpara
   fimpara
   
   escreval("Matriz Alterada:")
   para i de 0 ate N-1 faca
      para j de 0 ate N-1 faca
         escreva(mat[i, j]:3:1, " ")
      fimpara
      escreval
   fimpara
   

Fimalgoritmo