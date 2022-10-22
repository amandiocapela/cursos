sexo = input('Informe seu sexo [M/F]: ').strip().upper()
while 'M' != sexo != 'F':
    sexo = input('Dados inválidos! Informe seu sexo [M/F]: ').upper()
print(f'Sexo {sexo} registrado com sucesso.')