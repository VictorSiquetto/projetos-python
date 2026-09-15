from rich import *
import time

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f":book: [blue]Voce acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas} paginas[/] no total. Voce agora esta na [yellow]pagina {self.pagina_atual}[/][/]")

    def avancar_pagina(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end=' ')
                time.sleep(0.3)
                cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]pagina {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/red]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro('Livro Legal', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(50)

# def avancar_pagina(self, p = 1):
    #     if self.pagina_atual + p+1 <= self.paginas:
    #         for i in range(self.pagina_atual, self.pagina_atual + p+1):
    #             print(f"Pag{i} :right_arrow: ", end = " ")
    #             time.sleep(0.2)
    #         self.pagina_atual += p
    #         print(f"[blue]Voce avancou {p} paginas no total e agora esta na[/] [yellow]pagina {self.pagina_atual}[/]")
    #     else:
    #         for i in range(self.pagina_atual, self.paginas+1):
    #             print(f"Pag{i} :right_arrow: ", end = " ")
    #             time.sleep(0.2)
    #         print(f"[blue]Voce avancou {self.paginas - self.pagina_atual} paginas no total e agora esta na[/] [yellow]pagina {self.paginas}[/]")
    #         print(f":rotating_light: [red]Voce chegou ao final do livro '{self.titulo}'[/]")