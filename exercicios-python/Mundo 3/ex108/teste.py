# Exercício 108 – Formatando Moedas em Python

import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 13))}')
print(f'Diminuindo 15% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 15))}')
