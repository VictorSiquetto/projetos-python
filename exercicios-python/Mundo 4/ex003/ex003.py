from rich import *
from rich.panel import Panel

class Churrasco:

    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
    
    def __str__(self):
        return f'Esse é o {self.titulo} com {self.pessoas} participantes'
        
    def quantidade_carne(self) -> float:
        return self.pessoas * Churrasco.consumo_padrao

    def custo_total(self) -> float:
        return self.quantidade_carne() * Churrasco.preco_kg

    def custo_pessoa(self) -> float:
        return self.custo_total() / self.pessoas

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n'
        conteudo += f'Cada participante comera {Churrasco.consumo_padrao:.1f}Kg e cada Kg custa R${Churrasco.preco_kg:.2f}\n'
        conteudo += f'Recomendo [blue]comprar {self.quantidade_carne():.3f}Kg[/] de carne\n'
        conteudo += f'O custo total sera de [green]R${self.custo_total():.2f}[/]\n'
        conteudo += f'Cada pessoa pagara [yellow]R${self.custo_pessoa():.2f}[/] para participar'
        tabela = Panel(conteudo, title=self.titulo, width=70)
        print(tabela)

c1 = Churrasco('Churrasco dos Manos', 15)
c1.analisar()
c2 = Churrasco('Churrasco dos Amigos', 60)
c2.analisar()
