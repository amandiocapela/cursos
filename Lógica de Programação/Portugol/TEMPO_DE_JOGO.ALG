Algoritmo "tempo_de_jogo"


Var

    hi, hf : inteiro

Inicio

    escreval("Hora Inicial: ")
    leia(hi)
    escreval("Hora Final: ")
    leia(hf)

    se (hi > hf) ou (hi = hf) entao
        hf <- hf + 24
    fimse
    
    escreval("O jogo durou ", hf - hi , " hora(s)")


Fimalgoritmo
