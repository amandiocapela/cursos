Algoritmo "Miss�o Pr�tica N�vel 1"

Var

   n, divisor, divisores, somaPrimos, i : inteiro

Inicio

   divisor <- 1
   divisores <- 0
   somaPrimos <- 0
   escreva("Digite um valor: ")
   leia(n)
   
   para i de n ate 0 passo -1 faca

        enquanto divisor <= i faca
            se i % divisor = 0 entao
            divisores <- divisores + 1
            fimse
            divisor <- divisor + 1
        fimenquanto
        
        se divisores = 2 entao
            escreval("O n�mero ", i, " � primo")
            somaPrimos <- somaPrimos + i
        fimse

        divisores <- 0
        divisor <- 1
   
   fimpara
   
   escreval("A soma de todos os n�meros primos menores ou iguais a ", n, " �: ", somaPrimos)


Fimalgoritmo