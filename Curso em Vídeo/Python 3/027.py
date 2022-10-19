nome = input('Escreva seu nome: ').strip()

nm = nome.split()

print(f'''O nome digitado foi {nome}
O primeiro nome é {nm[0]}
O último nome é {nm[-1]}''')