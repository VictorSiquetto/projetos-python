# Exercício 61 – Progressão Aritmética v2.0

p = int(input('Qual o primeiro numero da PA: '))
r = int(input('Qual a razao da PA: '))
c = 1
while c <= 10:
    print(f'{p} -> ', end ='')
    p += r
    c += 1
print('Fim')
