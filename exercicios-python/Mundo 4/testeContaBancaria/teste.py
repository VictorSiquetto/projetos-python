class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso, saldo atual de R${self.saldo:.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo'
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:.2f} da conta {self.id}; SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'O saque no valor de R${valor:.2f} da conta {self.id} foi aprovado')

    def depositar(self, valor):
        self.saldo += valor
        print(f'O deposito no valor de R${valor:.2f} na conta {self.id} foi aprovado')
        
g1 = ContaBancaria(112, 'Cleber', 3000)
g1.depositar(2000)
g1.sacar(9000)
print(g1)