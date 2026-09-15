# Exercício 80 – Lista ordenada sem repetições

lista = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if num not in lista:
        if c == 0 or num > lista[-1]:
            lista.append(num)
            print('Valor adicionado no final da lista...')
        elif num < lista[0]:
            lista.insert(0, num)
            print('Valor adicionado na posicao 0...')
        else:
            for pos, p in enumerate(lista):
                if num < p:      # Percorre a lista: se o novo número for menor a um item da lista, ele "rouba" aquela posição e para a busca (break) 
                    lista.insert(pos, num)
                    print(f'Valor adicionado na posicao {pos}...')
                    break
    else:
        print('Valor repetido')
print('=-'*20)
print(f'Voce digitou os valores {lista}')
