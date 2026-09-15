# Exercício 75 – Análise de dados em uma Tupla

num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Voce digitou os numeros {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu primeiro na {num.index(3)+1}° posicao')
else:
    print('O numero 3 nao foi digitado')
print(f'Os valores pares foram ', end ='')
for c in num:
    if c % 2 == 0:
        print(c, end =' ')

# par = ()
# valores = ()
# for c in range(0, 4):
#     num = int(input('Digite um numero: '))
#     valores += (num,)
#     if num % 2 == 0:
#         par += (num,)
# print(f'Voce digitou os numeros {valores}')
# print(f'O valor 9 apareceu {valores.count(9)} vezes')
# if 3 in valores:
#     print(f'O valor 3 apareceu primeiro na {valores.index(3)+1}° posicao')
# else:
#     print('O numero 3 nao foi digitado')
# print(f'Os valores pares foram {par}')
