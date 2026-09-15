# Exercício 48 – Soma ímpares múltiplos de três

s = 0
cont = 0
for c in range(1, 501):                              # for c in range(1,501,2):
    if c % 2 != 0 and c % 3 == 0:                       #  if c % 3 == 0:
        print(c)                                           #   s += c
        cont += 1
        s += c
print(f'A soma dos {cont} numeros impares multiplos de 3 é {s}')
print('Fim')
