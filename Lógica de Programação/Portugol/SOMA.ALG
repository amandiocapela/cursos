Algoritmo "soma"

Var

   nome1, nome2 : caractere
   idade1, idade2 : inteiro
   idadeMedia: real

Inicio

   escreva("Nome: ")
   leia(nome1)
   escreva("Idade: ")
   leia(idade1)
   escreva("Nome: ")
   leia(nome2)
   escreva("Idade: ")
   leia(idade2)
   
   idadeMedia <- (idade1 + idade2) / 2
   
   escreval("Dados da primeira pessoa:")
   escreval("Nome = ", nome1)
   escreval("Idade = ", idade1)
   escreval("Dados da segunda pessoa:")
   escreval("Nome = ", nome2)
   escreval("Idade = ", idade2)
   escreval("A idade média de ", nome1, " e ", nome2, " é de ", idadeMedia, " anos")

Fimalgoritmo