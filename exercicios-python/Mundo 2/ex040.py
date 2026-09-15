# Exercício 40 – Aquele clássico da Média

nota1 = float(input('Qual foi sua primeira nota: '))
nota2 = float(input('Qual foi sua segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('Reprovado')
elif media >= 5 and media < 7:   # 7 > media >= 5:
    print('Recuperaçao')
else:
    print('Aprovado')
