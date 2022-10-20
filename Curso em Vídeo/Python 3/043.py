peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso / altura ** 2

if IMC < 18.5:
    print(f'Seu IMC é igual a {IMC:.1f} e você está abaixo do peso.')
elif 18.5 <= IMC < 25:
    print(f'Seu IMC é igual a {IMC:.1f} e você está no peso ideal.')
elif 25 <= IMC < 30:
    print(f'Seu IMC é igual a {IMC:.1f} e você está com sobrepeso.')
elif 30 <= IMC < 40:
    print(f'Seu IMC é igual a {IMC:.1f} e você está com obesidade.')
else:
    print(f'Seu IMC é igual a {IMC:.1f} e você está com obesidade mórmida.')