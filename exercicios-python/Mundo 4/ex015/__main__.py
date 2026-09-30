from classes import Credencial
from rich import *


def main():
    c = Credencial()
    try:
        c.senha = str(input("Digite a sua senha: "))
        print(c.senha)
        c.validar("senha123")
    except Exception as erro:
        print(f"[red]{erro}[/]")


if __name__ == "__main__":
    main()
