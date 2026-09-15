# Exercício 27 – Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome: ')).strip()
dividido = n.split()
print(f'Seu nome é {n}, seu primeiro nome é {dividido[0]} e seu ultimo nome é {dividido[len(dividido)-1]}')
