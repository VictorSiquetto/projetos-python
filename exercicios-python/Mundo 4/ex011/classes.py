from abc import ABC, abstractmethod
from rich import *
from rich.panel import Panel

class Funcionario(ABC):

    sal_min = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f"O salario de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{(self.salario/ Funcionario.sal_min):.1f} salarios minimos[/]."
        painel = Panel(conteudo, title="Analise de Salario", width=50)
        print(painel)


class Horista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = (self.valor_hora * self.horas_trab)
        inss = self.sal_bruto * Funcionario.inss / 100
        self.salario = self.sal_bruto - inss


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        inss = self.sal_bruto * Funcionario.inss / 100
        self.salario = self.sal_bruto - inss