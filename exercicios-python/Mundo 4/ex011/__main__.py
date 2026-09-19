from classes import *

def main():
    f1 = Horista("Joao", 14, 235)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Ana", 4700)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()