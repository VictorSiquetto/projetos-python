# Exercício 19 – Sorteando um item na lista

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print(f'O aluno sorteado foi {sorteado}.')
