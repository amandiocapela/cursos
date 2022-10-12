Algoritmo "terreno"

Var

   largura, comprimento, valorMetro, area, precoTerreno : real
   

Inicio

   escreva("Digite a largura do terreno:")
   leia(largura)
   escreva("Digite o comprimento do terreno:")
   leia(comprimento)
   escreva("Digite o valor do metro quadrado:")
   leia(valorMetro)
   
   area <- largura * comprimento
   precoTerreno <- area * valorMetro
   
   escreval("Area do terreno = ", area:8:2)
   escreval("Preco do terreno = ", precoTerreno:8:2)


Fimalgoritmo