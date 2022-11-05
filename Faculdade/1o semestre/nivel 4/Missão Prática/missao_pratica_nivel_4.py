# Classe para Despesas
class Despesas:
    def __init__(self, tipoDespesa, valorDespesa):
        self.tipoDespesa = tipoDespesa
        self.valorDespesa = valorDespesa

listaDespesas = []
dicDespesas = {}

while True:
    dicDespesas['Dia'] = int(input('Qual o dia? '))
    dicDespesas['Alimentação'] = int('Valor Gasto com Alimentação: R$')
    dicDespesas['Vestuário'] = int('Valor Gasto com Vestuário: R$')
    dicDespesas['Transporte'] = int('Valor Gasto com Transporte: R$')
    listaDespesas.append(dicDespesas.copy())
    dicDespesas.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
