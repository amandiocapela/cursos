M = 0
F = 0
soma = 0
maisVelhoIdade = 0
maisVelhoNome = ''
somaMulher20 = 0
for c in range(1,5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    if sexo == 'M' and idade > maisVelhoIdade:
        maisVelhoIdade = idade
        maisVelhoNome = nome
    if sexo == 'F' and idade < 20:
        somaMulher20 += 1
media = soma / 4

print(f'''A média de idade do grupo é de {media:.1f} anos
O homem mais velho tem {maisVelhoIdade} anos e se chama {maisVelhoNome}.
Ao todo são {somaMulher20} com menos de 20 anos.''')

