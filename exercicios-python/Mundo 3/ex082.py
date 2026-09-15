# Exercício 82 – Dividindo valores em várias listas

lista = []
lista_pares = []
lista_impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Digite uma opcao valida')
    if opcao == 'N':
        break
for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista dos pares é {lista_pares}')
print(f'A lista dos impares é {lista_impares}')
