from rich import *
from rich.panel import Panel

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista = []

    def add_favoritos(self, jogo):
        self.lista.append(jogo)
        self.lista = sorted(self.lista, key=str.lower)

    def ficha(self):
        conteudo = f"Nome Real: [on blue]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos: "
        for i in self.lista:
            conteudo += f"\n:video_game: [blue]{i}[/]"
        ficha = Panel(conteudo, title=f"Jogador <{self.nick}>", width=34)
        print(ficha)

p1 = Gamer("Joao Souza", "joaozin123")
p1.add_favoritos("God of Wars")
p1.add_favoritos("CSGO")
p1.ficha()

p2 = Gamer("Ana Silva", "aninha321")
p2.add_favoritos("The Sims")
p2.add_favoritos("Minecraft")
p2.add_favoritos("Fortnite")
p2.ficha()