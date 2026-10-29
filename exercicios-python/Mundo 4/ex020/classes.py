from abc import ABC, abstractmethod


class Arquivo(ABC):

    def __init__(self, nome: str, ext: str, tamanho: int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext: str):
        formatos = ["pdf", "doc", "docx"]
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError("Formato do arquivo nao suportado")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1000000}MB)"


class DOC(Arquivo):

    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "doc", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


class PDF(Arquivo):

    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")


def abrir_arquivo(arquivo):
    arquivo.abrir()
