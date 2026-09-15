# Exercício 90 – Dicionário em Python

nota = {}
nota['Nome'] = str(input('Nome: '))
nota['Media'] = float(input('Media: '))

if nota['Media'] >= 7:
    nota['Situacao'] = 'Aprovado'
elif 5 <= nota['Media'] < 7:
    nota['Situacao'] = 'Recuperacao'
else:
    nota['Situacao'] = 'Reprovado'

for k, v in nota.items():
    print(f'{k} é igual a {v}')
