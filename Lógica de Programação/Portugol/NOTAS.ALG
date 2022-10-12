Algoritmo "notas"

Var

   n1, n2, nf : real

Inicio

   escreval("Digite a primeira nota: ")
   leia(n1)
   escreval("Digite a segunda nota: ")
   leia(n2)

   nf <- n1 + n2
   
   escreval("Nota Final =", nf)
   se nf > 60.00 então
   escreval("Aprovado")
   senao
   escreval("Reprovado")
   fimse


Fimalgoritmo