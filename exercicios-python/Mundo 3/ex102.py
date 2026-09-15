# Exercício 102 – Função para Fatorial

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um Numero.
    param n: O numero a ser calculado.
    param show: (Opcional) Mostrar ou nao a conta.
    return: Retorna o fatorial do numero (n).
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end ='')
            print(' x ' if c > 1 else ' = ', end ='')
        f *= c
    return f

print(fatorial(5))
help(fatorial)
