# Exercício 84 – Lista composta e análise de dados

lista = []
lista_final = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(lista_final) == 0:
        maior = menor =lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    lista_final.append(lista[:])
    lista.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Digite uma opcao valida')
    if opcao == 'N':
        break
print('=-'*30)
print(f'Foram cadastradas {len(lista_final)} pessoas')
print(f'O maior peso foi {maior} Kg. Peso de ', end ='')
for p in lista_final:
    if p[1] == maior:
        print(f'[{p[0]}]', end =' ')
print(f'\nO menor peso foi {menor} Kg. Peso de ', end ='')
for p in lista_final:
    if p[1] == menor:
        print(f'[{p[0]}]', end =' ')
