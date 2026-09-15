# Exercício 22 – Analisador de Textos

nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiusculas é: {nome.upper()}')
print(f'Seu nome em minusculas é: {nome.lower()}')
print(f'Seu nome tem: {len(nome) - nome.count(' ')} letras')
nome = nome.split()
print(f'Seu primeiro nome tem: {len(nome[0])} letras')
