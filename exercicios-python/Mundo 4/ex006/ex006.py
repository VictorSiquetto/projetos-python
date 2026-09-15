from rich import *

class Caneta:

    def __init__(self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelha" | "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "amarela":
                escolha = "[yellow]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if not self.tampada:
            print(f"{self.cor}{texto}[/]", end=" ")
        else:
            print(f":prohibited: A {self.cor}caneta[/] esta tampada!")

    def quebrar_linha(self, num = 1):
        for i in range(0, num, 1):
            print()
        #print("\n" * num, end="")

c1 = Caneta("azul")
c1.escrever("ola")
c1.quebrar_linha()
c1.destampar()
c1.escrever("Ola Mundo")

c2 = Caneta("vermelha")
c2.destampar()
c2.escrever("Tudo Bem")

c3 = Caneta("verde")
c3.destampar()
c3.quebrar_linha(2)
c3.escrever("blablabla")