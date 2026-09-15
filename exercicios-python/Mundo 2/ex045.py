# Exercício 45 – GAME: Pedra Papel e Tesoura

from random import randint

print('''0) pedra
1) papel
2) tesoura''')
jogada = int(input('Qual sua jogada: '))

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print(f'Voce jogou {itens[jogada]}')
print (f'Eu joguei {itens[pc]}')

if pc == 0:
    if jogada == 2:
        print('Eu Ganhei')
    elif jogada == 1:
        print('Voce Ganhou')
    elif jogada == 0:
        print('Empate')
    else:
        print('Jogada Invalida')
elif pc == 1:
    if jogada == 2:
        print('Voce Ganhou')
    elif jogada == 1:
        print('Empate')
    elif jogada == 0:
        print('Eu Ganhei')
    else:
        print('Jogada Invalida')
elif pc == 2:
    if jogada == 1:
        print('Eu Ganhei')
    elif jogada == 0:
        print('Voce Ganhou')
    elif jogada == 2:
        print('Empate')
    else:
        print('Jogada Invalida')
