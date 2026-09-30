from hashlib import sha256


class ContaBancaria:

    def __init__(
        self, id: int, nome: str = None, saldo: float = 0, chave: str | int = None
    ):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(str(chave).encode("utf-8")).hexdigest()
        print(
            f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:.2f}"
        )

    def __str__(self):
        return (
            f"A conta {self._id} de {self._titular} tem R${self.__saldo:.2f} de saldo"
        )

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome: str = None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if len(novonome) >= 3:
                self._titular = novonome
        else:
            print("Senha incorreta, alteracao de nome nao autorizada")

    def validar_senha(self, senha) -> bool:
        usuario = sha256(str(senha).encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:

        from pwinput import pwinput

        while True:
            senha = pwinput("Senha: ").strip()
            if len(senha) >= 5:
                break
        return senha

    def sacar(self, valor: float, chave: str | int = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque negado de R${valor:.2f} na conta {self._id}")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} autorizado na conta {self._id}")
        else:
            print("Senha incorreta, saque nao autorizado")

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self._id}")
