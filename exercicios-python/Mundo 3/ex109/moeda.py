def dobro(num = 0, param=False):
    n = num * 2
    if param:
        return moeda(n)
    return n

def metade(num = 0, param=False):
    n = num / 2
    if param:
        return moeda(n)
    return n

def aumentar(num = 0, p = 0, param=False):
    n = num + (num * p / 100)
    if param:
        return moeda(n)
    return n

def diminuir(num = 0, p = 0, param=False):
    n = num - (num * p / 100)
    if param:
        return moeda(n)
    return n

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
