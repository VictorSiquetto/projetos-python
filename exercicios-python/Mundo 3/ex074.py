# Exercício 74 – Maior e menor valores em Tupla

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print('Os valores sorteados foram: ', end ='')
for c in numeros:
    print(c, end =' ')
print(f'\nO maior numero foi {max(numeros)}')
print(f'O menor numeto foi {min(numeros)}')

# from random import sample     para os numeros nao se repetirem

# numeros = sample(range(1, 11), 5)    
# print('Os valores sorteados foram: ', end ='')
# for c in numeros:
#     print(c, end =' ')
# print(f'\nO maior numero foi {max(numeros)}')
# print(f'O menor numeto foi {min(numeros)}')
