Algoritmo "media_ponderada"

Var

   n, i : inteiro
   v1, v2, v3, media : real

Inicio

   media <- 0

   escreva("Quantos casos você vai digitar? ")
   leia(n)

   para i de 1 ate n faca

      escreval("Digite três números: ")
      leia(v1)
      leia(v2)
      leia(v3)

      media <- ((v1*2) + (v2*3) + (v3*5)) / 10

      escreval("Média = ", media:1:1)
      
   fimpara

Fimalgoritmo