# Exercício 65 – Maior e Menor valores

# soma = maior = menor = 0
# c = 1
# num = int(input('Digite um numero: '))
# soma += num
# maior = num
# menor = num
# opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
# while opcao not in 'N':
#     c += 1
#     num = int(input('Digite um numero: '))
#     soma += num
#     if num > maior:
#         maior = num
#     if num < menor:
#         menor = num
#     opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
# media = soma / c
# print(f'Voce digitou {c} numeros a media foi {media:.2f}\nO maior valor foi {maior} e o menor valor foi {menor}')

resp = 'S'
soma = maior = menor = c = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
media = soma / c
print(f'Voce digitou {c} numeros a media foi {media:.2f}\nO maior valor foi {maior} e o menor valor foi {menor}')
