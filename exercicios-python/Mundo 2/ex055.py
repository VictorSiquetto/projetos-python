# Exercício 55 – Maior e menor da sequência

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.2f}Kg')
print(f'O menor peso lido foi {menor:.2f}Kg')
