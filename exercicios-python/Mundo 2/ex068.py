# Exercício 68 – Jogo do Par ou Ímpar

from random import randint

c = 0
while True:
    print('=-'*12)
    print('Vamos Jogar Par ou Impar')
    print('=-'*12)
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    if (jogador + pc) % 2 == 0:
        jogada = 'P'
    else:
        jogada = 'I'
    if opcao == jogada:
        print('--'*20)
        print(f'Voce jogou {jogador} e o computador {pc}, o total deu {jogador + pc} \nVoce venceu \nVamos jogar novamente...')
        print('--'*20)
        c += 1
    else:
        print('--'*23)
        print(f'Voce jogou {jogador} e o computador {pc}, o total deu {jogador + pc} \nVoce perdeu')
        print('--'*23)
        break
print(f'Game Over, voce venceu {c} vezes')
