# Exercício 17 – Catetos e Hipotenusa

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co,ca)
print(f'A hipotenusa vai medir {hip:.2f}')
