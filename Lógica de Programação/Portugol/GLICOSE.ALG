Algoritmo "glicose"

Var

   glicose : real
   classif : caracter

Inicio

   escreva("Digite a medida da glicose: ")
   leia(glicose)
   
   se glicose <= 100.0 entao
       classif <- "normal"
   senao
       se glicose <= 140.0 entao
       classif <- "elevado"
       senao
           classif <- "diabetes"
       fimse
   fimse
   
   escreval("Classificação : ", classif)


Fimalgoritmo