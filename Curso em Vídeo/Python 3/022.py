nome = input('Digite seu nome: ').strip()
print(f'''Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome)-nome.count(' ')} letras
Seu primeiro nome tem {len(nome.split()[0])} letras''')
