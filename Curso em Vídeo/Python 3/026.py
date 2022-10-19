frase = input('Digite uma frase: ')

print(f'A leta A aparece {frase.upper().count("A")} vezes. Ela aparece pela primeira vez na posição {frase.upper().find("A")+1} e pela última vez na posição {frase.upper().rfind("A")+1}.')
