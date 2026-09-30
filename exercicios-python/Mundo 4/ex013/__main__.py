from classes import Termostato



def main():
    t1 = Termostato()
    try:
        t1.temperatura = 21.5
    except Exception as erro:
        print(erro)

    print(f"A temperatura atual é {t1.ftemperatura}")

if __name__ == "__main__":
    main()