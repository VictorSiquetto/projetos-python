# Exercício 98 – Função de Contador

from time import sleep

def contador(i, f, p):
    print('=-'*16)
    if i < f:
        print(f'Contagem de {i} ate {f}, de {p} em {p}:')
    else:
        print(f'Contagem de {i} ate {f}, de {p*-1} em {p*-1}:')
    for c in range(i, f + 1, p):
        print(c, end =' ', flush=True)
        sleep(0.5)
    print('Fim')

contador(1, 10, 1)
contador(10, 0, -2)
print('=-'*16)
print('Agora é sua vez de personalizar a contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
