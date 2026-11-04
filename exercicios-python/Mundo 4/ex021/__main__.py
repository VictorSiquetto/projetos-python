from classes import *


def main():
    finalizar_compra(Pix(), 4500)
    finalizar_compra(Credito(), 340.99)
    finalizar_compra(Boleto(), 1_200.50)


if __name__ == "__main__":
    main()
