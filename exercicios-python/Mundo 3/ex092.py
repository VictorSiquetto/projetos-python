# Exercício 92 – Cadastro de Trabalhador em Python

from datetime import date

atual = date.today().year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = atual - nascimento
cadastro['ctps'] = int(input('Carteira da trabalho (0 nao tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratacao: '))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = ((cadastro['contratacao'] + 35) - atual) + cadastro['idade']
print('=-'*15)
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
