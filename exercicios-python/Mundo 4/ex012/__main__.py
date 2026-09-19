from classes import *

def main():
    g1 = Guerreiro("Kratos", 2000)
    m1 = Mago("Harry", 1450)

    g1.atacar(m1, 200)
    m1.atacar(g1)
    g1.curar()
    m1.curar()

    g1.status_personagem()
    m1.status_personagem()

if __name__ == "__main__":
    main()