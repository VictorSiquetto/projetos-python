# Exercício 51 – Progressão Aritmética

p = int(input('Qual o primeiro numero da PA: '))
r = int(input('Qual a razao da PA: '))
d = p + (11 - 1) * r         # d = decimo numero de uma PA
for c in range(p, d, r):     # d + r (outra opcao ao inves de trocar o 10 por 11 no d)
    print(c)
print('Fim')
