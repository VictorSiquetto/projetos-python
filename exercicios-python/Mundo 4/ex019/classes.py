from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self._salario = 0
        self.salario = salario

    def __str__(self):
        return f"{self.nome} ganha R${self._salario:.2f} e por ser {self.__class__.__name__} o bonus sera de R${self.calcular_bonus():.2f}"

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor: float):
        if valor >= self._salario:
            self._salario = valor
        else:
            raise ValueError("Voce nao pode diminuir o salario de um funcionario")

    @abstractmethod
    def calcular_bonus(self):
        pass


class Designer(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonus = self._salario * 0.08
        aumento = self._salario + bonus
        self._salario = aumento
        return bonus


class Gerente(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonus = self._salario * 0.15
        aumento = self._salario + bonus
        self._salario = aumento
        return bonus


class Desenvolvedor(Funcionario):

    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonus = self._salario * 0.1
        aumento = self._salario + bonus
        self._salario = aumento
        return bonus
