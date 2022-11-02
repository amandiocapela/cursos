from cliente import Cliente
from contas import Conta

cli1 = Cliente('123', 'João', 'Rua 1')
cli2 = Cliente('234', 'Maria', 'Rua 2')

c1 = Conta([cli1, cli2], 1, 0)

print('-' * 10)
c1.gerarSaldo()
print('-' * 10)
print(f'Depositando R$1500...')
c1.depositar(1500)
print('-' * 10)
c1.gerarSaldo()
print('-' * 10)
print('Sacando R$500...')
c1.sacar(500)
print('-' * 10)
c1.gerarSaldo()
print('-' * 10)
c1.extrato.extrato(c1.numero)

