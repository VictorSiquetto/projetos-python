# Exercício 109 – Formatando Moedas em Python

import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p, True))}')
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
print(f'Aumentando 13% de {moeda.moeda(p)} é {(moeda.aumentar(p, 13, True))}')
print(f'Diminuindo 15% de {moeda.moeda(p)} é {(moeda.diminuir(p, 15, True))}')
