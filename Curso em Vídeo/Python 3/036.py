valor = float(input('Qual o valor da casa que deseja comprar? R$'))
sal = float(input('Qual o seu salário? R$'))
tempo = int(input('Emquantos anos você pretende pagar? '))

mensal = valor / (tempo * 12)
perc = (mensal / sal) * 100

if perc <= 30:
    print(f'Empréstimo de R${valor:.2f}, com mensalidade de R${mensal:.2f} para pagamento em {tempo * 12} meses, aprovado!')
else:
    print(f'A mensalidade de R${mensal:.2f} respresenta {perc:.1f}% de sua renda mensal. Por isso, seu empréstimo de R${valor:.2f}, para pagamento em {tempo * 12} meses, não foi aprovado.')