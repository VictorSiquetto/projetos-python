from classes import *


def main():
    p1 = Produto("Caneta", 12.50)
    p2 = Produto("Borracha", 7.80)
    p3 = Produto("Caderno", 25)
    p4 = Produto("Estojo", 38)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p2
    c2 = c2 + c1

    print(c1)
    print(c2)


if __name__ == "__main__":
    main()
