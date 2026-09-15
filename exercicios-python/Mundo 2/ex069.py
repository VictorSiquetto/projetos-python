# Exercício 69 – Análise de dados do grupo

i = h = m = 0
while True:
    print('=-'*10)
    print('Cadastre Uma Pessoa')
    print('=-'*10)
    idade = int(input('Idade: '))
    if idade >= 18:
        i += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        h += 1
    if idade < 20 and sexo == 'F':
        m += 1
    opcao = ' '
    print('--'*12)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    print('--'*12)
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {i}')
print(f'Total de homens cadastrados: {h}')
print(f'Total de mulheres com menos de 20 anos: {m}')
