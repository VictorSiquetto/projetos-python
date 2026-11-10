from classes import *


def main():
    u = [
        Usuario("Pedro", "pedro.souza@gmail.com"),
        Usuario("Carlos", "carlinhos@outlook.com"),
    ]

    a = [
        Aluno("Ana", "Informatica", "3 periodo"),
        Aluno("Joao", "Biologia", "5 periodo"),
    ]

    exportar_dados(JSON(), u)
    exportar_dados(XML(), a)


if __name__ == "__main__":
    main()
