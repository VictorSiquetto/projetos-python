# Exercício 112 – Entrada de dados monetários

from moeda import moeda
from dado import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 18, 10)
