from rich import *
from rich.panel import Panel


class Mensagem:

    def __init__(
        self, msg: str = "", tipo: str = "aviso", icone: str = ":speech_balloon:"
    ):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        painel = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            width=40,
            style="on black",
        )
        print(painel)


class Erro(Mensagem):

    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="erro", icone=":prohibited:")

    def mostrar(self):
        painel = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            width=40,
            style="yellow on red",
        )
        print(painel)


class Alerta(Mensagem):

    def __init__(self, msg: str = ""):
        super().__init__(msg, tipo="alerta", icone=":warning:")

    def mostrar(self):
        painel = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo.upper()} {self._icone}",
            width=40,
            style="black on yellow",
        )
        print(painel)
