# Exercício 70 – Estatísticas em produtos

s = p = c = 0
while True:
    print('=-'*10)
    print('Loja Super Baratao')
    print('=-'*10)
    c += 1
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    if c == 1:
        menor = nome
        menor_preco = preco
    else:
        if preco < menor_preco:
            menor = nome
            menor_preco = preco
    s += preco
    if preco > 1000:
        p += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        print('-'*12, 'Fim do Programa', '-'*12)
        break
print(f'O total da compra foi de R${s:.2f}')
print(f'Temos {p} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {menor} que custou {menor_preco:.2f}')
