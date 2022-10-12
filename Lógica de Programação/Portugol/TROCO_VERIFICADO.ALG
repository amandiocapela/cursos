Algoritmo "troco_verificado"

Var

   preco, recebido, troco, total : real
   qtd : inteiro

Inicio

      escreva("Preço unitário do produto :")
      leia(preco)
      escreva("Quantidade comprada :")
      leia(qtd)
      escreva("Dinheiro recebido :")
      leia(recebido)
      
      total <- qtd * preco
      troco <- recebido - total
      
      se troco >= 0 então
      escreval("Troco = R$", troco:1:2)
      senao
      escreval("Dinheiro insuficiente. Faltam R$", -troco:1:2)
      fimse
      
Fimalgoritmo
