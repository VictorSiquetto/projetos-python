from rich import *
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5


    def __init__(self, canal = 1, volume = 2):
        self.ligada: bool = False
        self.volume_atual: int = volume
        self.canal_atual: int = canal

    def liga_deslgia(self):
        self.ligada = not self.ligada

    def mostrar_tv(self):
        if not self.ligada:
            conteudo = f":prohibited: [red]A TV esta desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

    def canal_mais(self):
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligada:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1


    def volume_menos(self):
        if self.ligada:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1
                

tv = ControleRemoto()
while True:
    tv.mostrar_tv()
    comando = str(input(f"< CH{tv.canal_atual} >  - VOL{tv.volume_atual} + "))
    match comando:
        case "0":
            break
        case "@":
            tv.liga_deslgia()
        case ">":
            tv.canal_mais()
        case "<":
            tv.canal_menos()
        case "-":
            tv.volume_menos()
        case "+":
            tv.volume_mais()