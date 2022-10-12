Algoritmo "par_impar"

Var

   n, i, x : inteiro
   pn, ip : caractere

Inicio

    escreva("Quantos numeros voce vai digitar? ")
    leia(n)
    
    para i de 1 ate n faca
        escreva("Digite um número: ")
        leia(x)
        
       se x = 0 entao
           escreval("Nulo")
       senao
           se x % 2 = 0 entao
               se x < 0 entao
                   escreval("Par Negativo")
               senao
                   escreval("Par Positivo")
               fimse
           senao
               se x < 0 entao
                   escreval("Impar Negativo")
               senao
                   escreval("Impar Positivo")
               fimse
           fimse
       fimse
    fimpara


Fimalgoritmo