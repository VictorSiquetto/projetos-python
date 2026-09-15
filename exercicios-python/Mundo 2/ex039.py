# Exercício 39 – Alistamento Militar

from datetime import date

ano = int(input('Em que ano voce nasceu? '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    print(f'Voce ainda vai se alistar, sera em {atual + (18 - idade)}, ainda faltam {18 - idade} anos')
elif idade == 18:
    print('Esta na hora de se alistar')
else:
    print(f'Passou do tempo de se alistar, era em {atual - (idade - 18)}, ja passaram {idade - 18} anos')
