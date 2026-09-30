from rich import *


class Diario:

    def __init__(self, senha="CeV!@"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha=None):
        if senha == self.__senha:
            print(f"[green]Diário LIBERADO![/]")
            for i in self.__segredos:
                print(f"- {i}")
        else:
            raise PermissionError("Senha Inválida! Você não pode ler meu diário")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha")

    @senha.setter
    def senha(self, novasenha):
        self.__senha = novasenha.strip()
