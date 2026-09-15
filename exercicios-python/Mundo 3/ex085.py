# Exercício 85 – Listas com pares e ímpares

lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('=-'*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados fomam: {lista[1]}')
