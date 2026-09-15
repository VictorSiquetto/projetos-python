# Exercício 100 – Funções para sortear e somar

from random import randint
from time import sleep

lista = []
pares = []
def sorteia(l):
    for c in range(0, 5):
        l.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end ='')
    for c in l:
        print(f'{c}', end =' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def par(l):
    for c in l:
        if c % 2 == 0:
            pares.append(c)
    print(f'Somando os valores pares de {l}, temos {sum(pares)}', end ='')

sorteia(lista)
par(lista)
