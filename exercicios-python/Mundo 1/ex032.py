# Exercício 32 – Ano Bissexto

from datetime import date

ano = int(input('Digite o ano que voce deseja analisar, coloque 0 caso queira analisar o ano autal: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é Bissexto')
else:
    print('O ano nao é Bissexto')
