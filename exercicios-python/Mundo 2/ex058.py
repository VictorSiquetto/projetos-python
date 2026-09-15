# Exercício 58 – Jogo da Adivinhação v2.0

from random import randint

print('Sou seu computador... \nAcabei de pensar em um numero entre 0 e 10. \nVoce consegue adivinhar qual é?')
numero_pc = randint(0,10)
numero_usuario = int(input('Qual o seu palpite? '))
while numero_usuario != numero_pc:
    if numero_usuario > numero_pc:
        print('Menos... Tente mais uma vez.')
        numero_usuario = int(input('Qual o seu palpite? '))
    elif numero_usuario < numero_pc:
        print('Mais... Tente mais uma vez.')
        numero_usuario = int(input('Qual o seu palpite? '))
print(f'Parabens voce acertou o meu numero era {numero_pc}')        
