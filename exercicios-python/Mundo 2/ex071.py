# Exercício 71 – Simulador de Caixa Eletrônico

cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
while True:
    print('=-'*15)
    print(f'{'Banco Dev':^30}')
    print('=-'*15)
    valor = int(input('Qual valor voce quer sacar: '))
    if valor >= 50:
        cedulas_50 = valor // 50
        if cedulas_50 >= 1:
            print(f'valor de {cedulas_50} cedulas de R$50')
        valor = valor % 50
    if valor >= 20:
        cedulas_20 = valor // 20
        if cedulas_20 >= 1:
            print(f'valor de {cedulas_20} cedulas de R$20')
        valor = valor % 20
    if valor >= 10:
        cedulas_10 = valor // 10
        if cedulas_10 >= 1:
            print(f'valor de {cedulas_10} cedulas de R$10')
        valor = valor % 10
    if valor >= 1:
        cedulas_1 = valor // 1
        if cedulas_1 >= 1:
            print(f'valor de {cedulas_1} cedulas de R$1')
        valor = 0
    if valor == 0:
        break
print('=-'*15)
print('Volte sempre ao Banco Dev')
