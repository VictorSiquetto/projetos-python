# Exercício 107 – Exercitando módulos em Python

import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Aumentando 13% de {p} é {moeda.aumentar(p, 13)}')
print(f'Diminuindo 15% de {p} é {moeda.diminuir(p, 15)}')
