# Exercício 91 – Jogo de Dados em Python

from random import randint
from time import sleep
from operator import itemgetter

dado = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print('VALORES SORTEADOS:')
for k, v in dado.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('=-'*15)
print('=== RANKING DOS JOGADORES ===')
ranking = []
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar = {v[0]} com {v[1]}')
    sleep(1)
