from classes import Retangulo
from rich import *


def main():
    r = Retangulo()
    try:
        r.base = 8
        r.altura = 6
        r.medidas = (12, 5)
    except Exception as erro:
        print(f"[red]{erro}[/]")

    print(r.medidas)


if __name__ == "__main__":
    main()
