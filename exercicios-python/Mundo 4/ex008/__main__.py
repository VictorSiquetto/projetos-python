from classes import *
from rich import *

def main():
    q = Quadrado(25)
    c = Circulo(12)

    print(f"Perimetro do Quadrado = {q.perimetro():.2f}")
    print(f"Area do Quadrado = {q.area():.2f}")
    print(f"Perimetro do Circulo = {c.perimetro():.2f}")
    print(f"Area do Circulo = {c.area():.2f}")

if __name__ == "__main__":
    main()