Algoritmo "experiencias"

Var

   n, i, qtd, c, r, s, soma : inteiro
   percC, percR, percS : real
   cobaia : caractere

Inicio

   c <- 0
   r <- 0
   s <- 0
   
   escreva("Quantos casos de teste serão digitados? ")
   leia(n)
   
   para i de 1 ate n faca
      escreva("Quantidade de cobaias: ")
      leia(qtd)
      escreva("Tipo de cobaia: ")
      leia(cobaia)

      se cobaia = "c" entao
          c <- c + qtd
      senao
          se cobaia = "r" entao
              r <- r + qtd
          senao
              s <- s + qtd
          fimse
      fimse

   fimpara
   
   soma <- c + r + s
   percC <- c / soma * 100
   percR <- r / soma * 100
   percS <- s / soma * 100
   
   escreval("Relatório Final:")
   escreval("Total: ", soma, " cobaias")
   escreval("Total de Coelhos: ", c)
   escreval("Total de Ratos: ", r)
   escreval("Total de Sapos: ", s)
   escreval("Percentual de Coelhos: ", percC:1:2)
   escreval("Percentual de Ratos: ", percR:1:2)
   escreval("Percentual de Sapos: ", percS:1:2)

Fimalgoritmo