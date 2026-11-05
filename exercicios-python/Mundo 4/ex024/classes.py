from abc import ABC, abstractmethod
import re


class Validador(ABC):

    @abstractmethod
    def validar(self, valor: str) -> bool:
        pass


class Usuario(Validador):

    def validar(self, valor: str) -> bool:
        if re.fullmatch(r"^[a-z0-9_]{5,20}$", valor):
            return True
        else:
            return False


class Email(Validador):

    def validar(self, valor: str) -> bool:
        if re.fullmatch(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$", valor):
            return True
        else:
            return False


class Senha(Validador):

    def validar(self, valor: str) -> bool:
        if re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$", valor):
            return True
        else:
            return False


def validar_dado(validador: Validador, valor: str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é valido? {'SIM' if resultado else 'NAO'}")
