Algoritmo "circulo"

Var

   nome : caracter
   valorHora, pagamento : real
   horasTrabalhadas : inteiro

Inicio

   escreva("Nome: ")
   leia(nome)
   escreva("Valor por hora: ")
   leia(valorHora)
   escreva("Horas trabalhadas: ")
   leia(horasTrabalhadas)
   
   pagamento <- valorHora * horasTrabalhadas
   
   escreva("O pagamento para ", nome, "deve ser ", pagamento:8:2)

Fimalgoritmo