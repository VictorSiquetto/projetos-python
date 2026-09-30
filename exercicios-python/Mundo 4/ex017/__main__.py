from classes import ContaBancaria


def main():
    c = ContaBancaria(4444, "Joao", 5000, 12345)

    c.depositar(2000)
    c.sacar(250)
    c.nome = "Carlos"
    print(c)


if __name__ == "__main__":
    main()
