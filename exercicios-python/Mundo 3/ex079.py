# Exercício 79 – Valores únicos em uma Lista

lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Letra invalida tente novamente')
    if opcao == 'S':
        print('Valor inserido com sucesso...')
    if opcao in 'N':
        break 
lista.sort()
print('=-'*20)
print(f'Voce digitou os valores {lista}')
