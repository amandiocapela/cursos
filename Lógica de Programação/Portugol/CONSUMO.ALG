Algoritmo "consumo"

Var

   distancia : inteiro
   combustivel, consumo : real

Inicio

   escreva("Distancia percorrida: ")
   leia(distancia)
   escreva("Combustível gasto: ")
   leia(combustivel)
   
   consumo <- distancia / combustivel
   
   escreva("Consumo medio = ", consumo:8:3)

Fimalgoritmo