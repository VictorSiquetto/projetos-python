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

def resumo(num = 0, pa = 0, pd = 0):
    print('--'*18)
    print(f'{'RESUMO DO VALOR':^36}')
    print('--'*18)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{(dobro(num, True))}')
    print(f'Metade do preço: \t{(metade(num, True))}')
    print(f'{pa}% de aumento: \t{(aumentar(num, pa, True))}')
    print(f'{pd}% de reducao: \t{(diminuir(num, pd, True))}')
    print('--'*18)
    