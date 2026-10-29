from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome: str, salario: float = 1600):
        self.nome = nome
        self.__salario = salario

    def __str__(self):
        return f"{self.nome} ganha R${self.__salario:.2f} e por ser {self.__class__.__name__} o bonus sera de R${self.calcular_bonus():.2f}"

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor: float = None):
        if valor is None:
            raise ValueError("Impossivel reajustar o salario sem um valor")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Voce nao pode diminuir o salario de um funcionario")

    @abstractmethod
    def calcular_bonus(self):
        pass


class Designer(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.08


class Gerente(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.15


class Desenvolvedor(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.1
