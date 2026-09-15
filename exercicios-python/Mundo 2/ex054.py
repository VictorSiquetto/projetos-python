# Exercício 54 – Grupo da Maioridade

from datetime import date

hoje = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = hoje - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade')
