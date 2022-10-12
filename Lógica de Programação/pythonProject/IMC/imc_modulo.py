print("Módulo importado!")
def calcula_imc(peso, altura):
    print(f"Parâmetro peso: {peso}")
    print(f"Parâmetro altura: {altura}")
    imc = float(peso)/float(altura) ** 2
    return imc

def classifica_imc(indice):
    if indice < 18.5:
        return "Baixo Peso"
    elif indice < 25:
        return "Peso adequado"
    elif indice < 30:
        return "Sobrepeso"
    else:
        return "Obeso"
