from rich import *

class Funcionario:

    empresa = 'Curso em Video'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self) -> str:
        return f':waving_hand: Ola, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'  #{self.__class__.empresa}
    
c1 = Funcionario('Maria', 'Administracao', 'Diretora')
print(c1.apresentar())
c2 = Funcionario('Jose', 'TI', 'Programador')
print(c2.apresentar())
