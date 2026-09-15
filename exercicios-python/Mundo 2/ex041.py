# Exercício 41 – Classificando Atletas

from datetime import date
atual = date.today().year

nasc = int(input('Em que ano voce nasceu? '))
idade = atual - nasc

if idade <= 9:
    print('Mirim')
elif idade <=14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
