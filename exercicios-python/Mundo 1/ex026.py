# Exercício 26 – Primeira e última ocorrência de uma string

n = str(input('Digite seu nome: ')).lower().strip()
print(n.count('a'))
print(n.find('a')+1)
print(n.rfind('a')+1 - n.count(' '))
