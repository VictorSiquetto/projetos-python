# Exercício 81 – Extraindo dados de uma Lista

lista = []
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
lista.sort(reverse=True)
print('=-'*20)
print(f'Voce digitou {len(lista)} elementos')
print(f'Os valores em ordem decresente sao {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 nao foi encontrado na lista')
