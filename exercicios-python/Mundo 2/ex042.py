# Exercício 42 – Analisando Triângulos v2.0

n1 = float(input('Valor do 1° segmento: '))
n2 = float(input('Valor do 2° segmento: '))
n3 = float(input('Valor do 3° segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode formar um Triangulo ', end='')
    if n1 == n2 and n2 == n3:
        print('Equilatero')
    elif n1 != n2 and n1 != n3 and n2 != n3:        
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Nao pode formar um triangulo')
