# Exercício 33 – Maior e menor valores

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
print(f'Maior numero é {maior}')
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
print(f'Menor numero é {menor}')
