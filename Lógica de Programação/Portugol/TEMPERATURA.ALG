Algoritmo "temperatura"

Var

    escala : caractere
    c, f: real

Inicio

    escreva("Você vai digitar a temperatura em qual escala (C/F)? ")
    leia(escala)
    
    se (escala = "C") ou (escala = "c") entao
        escreva("Digite a temperatura em Celsius: ")
        leia(c)
        f <- 9 * c / 5 - 32
        escreval("Temperatura equivalente em Fahrenheit: ", f:1:2)
    senao
        escreva("Digite a temperatura em Fahrenheit: ")
        leia(f)
        c <- 5 / 9 * (f - 32)
        escreval("Temperatura equivalente em Fahrenheit: ", c:1:2)
    fimse

    
    
Fimalgoritmo