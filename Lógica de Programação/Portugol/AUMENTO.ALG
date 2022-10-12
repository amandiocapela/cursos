Algoritmo "aumento"


Var

    salario_atual, salario_novo, aumento : real

Inicio

    escreva("Digite o salário da pessoa: ")
    leia(salario_atual)
    
    se salario_atual <= 1000.00 entao
        salario_novo <- salario_atual * 1.2
        aumento <- salario_novo - salario_atual
        escreval("Novo salário = R$", salario_novo:8:2)
        escreval("Aumento = ", aumento:8:2)
        escreval("Porcentagem = 20%")
    senao
        se salario_atual <= 3000.00 entao
            salario_novo <- salario_atual * 1.15
            aumento <- salario_novo - salario_atual
            escreval("Novo salário = R$", salario_novo:8:2)
            escreval("Aumento = ", aumento:8:2)
            escreval("Porcentagem = 15%")
    senao
        se salario_atual <= 8000.00 entao
            salario_novo <- salario_atual * 1.1
            aumento <- salario_novo - salario_atual
            escreval("Novo salário = R$", salario_novo:8:2)
            escreval("Aumento = ", aumento:8:2)
            escreval("Porcentagem = 10%")
    senao
        salario_novo <- salario_atual * 1.05
            aumento <- salario_novo - salario_atual
            escreval("Novo salário R$= ", salario_novo:8:2)
            escreval("Aumento = ", aumento:8:2)
            escreval("Porcentagem = 5%")
        fimse
        fimse
    fimse

Fimalgoritmo
