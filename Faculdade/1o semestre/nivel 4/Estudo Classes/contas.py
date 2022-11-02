import datetime
from extrato import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.__saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato = Extrato()

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('Saldo Inválido')
        else:
            self.__saldo = saldo
    def depositar(self, valor):
        self.__saldo += valor
        self.extrato.transacoes.append(['DEPÓSITO', valor, 'Data', datetime.datetime.today()])

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, 'Data', datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.__saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.__saldo -= valor
            self.extrato.transacoes.append(['TRANSFERÊNCIA', valor, 'Data', datetime.datetime.today()])
        return ('Transferência Realizada')

    def gerarSaldo(self):
        print(f'Número: {self.numero} \nSaldo: R${self.__saldo:.2f}')
