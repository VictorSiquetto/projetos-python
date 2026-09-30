from rich import *
from classes import Diario


def main():
    d1 = Diario()
    try:
        d1.escrever("aaaaaa")
        d1.escrever("bbbbbb")
        d1.escrever("cccccc")
        d1.ler("CeV!@")
    except Exception as erro:
        print(f"[red]{erro}[/]")


if __name__ == "__main__":
    main()
