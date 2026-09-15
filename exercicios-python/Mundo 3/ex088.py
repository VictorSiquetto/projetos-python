# Exercício 88 – Palpites para a Mega Sena

from random import randint
from time import sleep

print('=-'*14)
print('     JOGA NA MEGA SENA     ')
print('=-'*14)
num = int(input('Quantos jogos voce quer que eu sorteie: '))
print(f'=-=-=- SORTEANDO {num} JOGOS -=-=-=')
for c in range(1, num+1):
    lista = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), ]
    print(f'Jogo {c}: {lista}')
    sleep(1)
print('=-=-=- BOA SORTE -=-=-=')

# lista = []
# jogos= []
# print('=-'*14)
# print('     JOGA NA MEGA SENA     ')
# print('=-'*14)
# quant = int(input('Quantos jogos voce quer que eu sorteie: '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1, 60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print(f'=-=-=- SORTEANDO {quant} JOGOS -=-=-=')
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
# print('=-=-=- BOA SORTE -=-=-=')