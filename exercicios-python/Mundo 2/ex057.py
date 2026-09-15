# Exercício 57 – Validação de Dados

sexo = str(input('Qual o seu sexo (M/F)? ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo (M/F): ')).strip().upper()[0]
print(f'O seu sexo é {sexo}, e ele foi registrado com sucesso')
