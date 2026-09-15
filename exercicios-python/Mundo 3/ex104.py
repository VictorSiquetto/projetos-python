# Exercício 104 – Validando entrada de dados em Python

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero valido')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
