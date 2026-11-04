from abc import ABC, abstractmethod
import locale


class Pagamento(ABC):

    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Insira um valor positivo")

    @property
    def fvalor(self):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self, tipo, valor: float):
        pass


class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Boleto"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Boleto"


class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Pix"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Pix"


class Credito(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.fvalor} via Credito"
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via Credito"


def finalizar_compra(tipo, valor: float):
    print(tipo.pagar(valor))
