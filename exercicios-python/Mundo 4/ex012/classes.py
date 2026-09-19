from abc import ABC, abstractmethod
import random
from rich import *
from rich.panel import Panel

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[blue]{self.nome}({self.vida})[/] atacou [red]{alvo.nome}({alvo.vida})[/] com um [green]{golpe}[/] de forca [yellow]{forca}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} nao pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[red]{self.nome}[/] recebeu dano de [yellow]{fator}[/]")

    @abstractmethod
    def curar(self):
        pass

    def status_personagem(self):
        conteudo = f"Nome: [blue]{self.nome}[/]\n"
        conteudo += f"Vida: [green]{self.vida}[/]\n"
        conteudo += f"Golpes: "
        for g in self.golpes:
            conteudo += f"\n:boxing_glove: [red]{g}[/]" 
        painel = Panel(conteudo, title=f"{type(self).__name__}", width=35)
        print(painel)


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Golpe Mortal", "Torvelinho", "Investida Corajosa"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{fator}[/] pontos de vida")


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Míssil Arcano", "Nova de Gelo"]
    
    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] fez uma magia de cura e recuperou [green]{fator}[/] pontos de vida")