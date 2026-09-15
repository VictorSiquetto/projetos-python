# Exercício 87 – Mais sobre Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
terceira = []
maior = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valora para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par.append(matriz[linha][coluna])
        if matriz[linha][2]:
            terceira.append(matriz[linha][2])
        if matriz[1][coluna]:
            maior.append(matriz[1][coluna])
print('=-'*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end ='')
    print()
print('=-'*20)
print(f'A soma dos valores pares é {sum(par)}')
print(f'A soma dos valores da terceira coluna é {sum(terceira)}')
print(f'O maior valor da segunda linha é {max(maior)}')
