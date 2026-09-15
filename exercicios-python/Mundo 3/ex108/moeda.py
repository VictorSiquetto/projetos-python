def dobro(num = 0):
    n = num * 2
    return n

def metade(num = 0):
    n = num / 2
    return n

def aumentar(num = 0, p = 0):
    n = num + (num * p / 100)
    return n

def diminuir(num = 0, p = 0):
    n = num - (num * p / 100)
    return n

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
