Algoritmo "menor_de_tres"

Var

   v1, v2, v3, menor : inteiro

Inicio

  escreva("Primeiro valor: ")
  leia(v1)
  escreva("Segundo valor: ")
  leia(v2)
  escreva("Terceiro valor: ")
  leia(v3)


  se (v1 < v2) e (v1 < v3) entao
     menor <- v1
  senao
     se v2 < v3 entao
        menor <- v2
     senao
        menor <- v3
     fimse
  fimse
  
  escreval("Menor = ", menor)

  

Fimalgoritmo