# Exercício 49 – Tabuada v.2.0

n = int(input('Escolha um numero da tabuada: '))
for c in range(1, 11):
    r = n * (c)
    print(f'{n} x {c:2} = {r}')
print('Fim')
