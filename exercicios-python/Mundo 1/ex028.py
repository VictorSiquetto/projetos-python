# Exercício 28 – Jogo da Adivinhação v.1.0

from random import randint

print('~'*33)
print('IREI ESCOLHER UM NUMERO DE 0 A 5')
print('~'*33)
num = randint(0,5)
num1 = int(input('Digite o numero que voce acha que foi escolhido: '))

if num1 == num:
    print('Parabens voce acertou')
else:
    print(f'Voce Errou era {num}')
