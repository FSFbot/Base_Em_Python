class ContaBancaria:
    def __init__(self,titular, saldo_inicial):
        self.titular = titular
        
        self._saldo = saldo_inicial
        print(f"Conta de {self.titular} criada com saldo inicial de R$ {self._saldo:.2f}")
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Deposito de R {valor:.2f} realizado com sucesso")
        else:
            print("Error: o valor do deposito deve ser positovo")
    def sacar(self,valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser prositivo")
        elif valor > self._saldo:
            print(f"Error: Saldo insulficiente para sacar R${valor:.2f}")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso")
            self.consultar_saldo()
    def consultar_saldo(self):
        print(f"Saldo atual: R: {self._saldo:.2f}")


minha_conta = ContaBancaria("João da Silva", 1000.00)
print("\n ----Operaçoes-----")
minha_conta.consultar_saldo()
minha_conta.depositar(550.50)
minha_conta.sacar(200)
minha_conta.sacar(2000)