# Exercício 35 – Analisando Triângulo v1.0

n1 = float(input('Valor do 1° segmento: '))
n2 = float(input('Valor do 2° segmento: '))
n3 = float(input('Valor do 3° segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode formar um triangulo')
else:
    print('Nao pode formar um triangulo')
