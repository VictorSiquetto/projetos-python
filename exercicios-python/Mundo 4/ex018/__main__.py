from classes import *


def main():
    a = Aluno("Ana", 2009, "ADS")
    b = Aluno("Pedro", 2007, "MED")

    a.add_curso("BIO")

    print(b.idade)
    print(b.cursos_oficiais)
    print(a.__dict__)


if __name__ == "__main__":
    main()
