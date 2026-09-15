# Exercício 113 – Funções aprofundadas em Python

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor digite um numero inteiro valido\033[0m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mERRO: usuario preferiu nao digitar esse numero\033[0m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor digite um numero real valido\033[0m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mERRO: usuario preferiu nao digitar esse numero\033[0m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1:.1f} e o real foi {n2:.1f}')
