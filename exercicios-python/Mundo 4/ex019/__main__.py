from classes import *


def main():
    f1 = Designer("Joao", 1500)
    f2 = Gerente("Ana", 1500)
    f3 = Desenvolvedor("Carlos", 1500)

    f2.salario = 2200

    print(f1)
    print(f2)
    print(f3)


if __name__ == "__main__":
    main()
