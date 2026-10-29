from classes import *


def main():
    funcionarios = [
        Designer("Joao", 1500),
        Gerente("Ana", 1500),
        Desenvolvedor("Carlos", 1500),
    ]

    try:
        funcionarios[1].salario = 2200
    except Exception as e:
        print(f"ERRO: {e}")

    for f in funcionarios:
        print(f)


if __name__ == "__main__":
    main()
