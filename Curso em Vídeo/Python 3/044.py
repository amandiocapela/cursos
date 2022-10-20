valorI = float(input('Qual o valor do produto? R$'))

print('''Escolha a forma de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Digite o número da opção escolhida: '))

perc = 0
valorF = 0
if opcao == 1:
    perc = 0.9
    valorF = valorI * perc
    print(f'Você terá um desconto de 10% e o valor ficará em R${valorF:.2f}')
elif opcao == 2:
    perc = 0.95
    valorF = valorI * perc
    print(f'Você terá um desconto de 5% e o valor ficará em R${valorF:.2f}')
elif opcao == 3:
    perc = 1
    valorF = valorI * perc
    print(f'O valor ficará em R${valorF:.2f}')
elif opcao == 4:
    perc = 1.2
    valorF = valorI * perc
    print(f'Você terá um acréscimo de 20% e o valor ficará em R${valorF:.2f}')
else:
    print(f'A opção {opcao} não é valida.')