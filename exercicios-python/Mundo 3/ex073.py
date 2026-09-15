# Exercício 73 – Tuplas com Times de Futebol

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Red Bull Bragantino', 
         'Atlético Mineiro', 'Santos', 'Corinthians', 'Vasco da Gama', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print('=-'*40)
print(f'Lista de times do Brasileirao: {times}')
print('=-'*40)
print(f'Os cinco primeiros sao: {times[:5]}')
print('=-'*40)
print(f'Os quatro ultimos sao: {times[-4:]}')
print('=-'*40)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=-'*40)
print(f'O Sao Paulo esta na {times.index('São Paulo')+1}° posicao')


# print('=-'*40)
# print(f'Lista de times do Brasileirao: ', end ='')
# for c in times:
#     print(c, end =' ')
# print()
# print('=-'*40)

# print(f'Os cinco primeiros sao: ', end='')
# for c in times[:5]:
#     print(c, end =' ')
# print()
# print('=-'*40)

# print(f'Os quatro ultimos sao: ', end ='')
# for c in times[-4:]:
#     print(c, end =' ')
# print()
# print('=-'*40)

# print(f'Times em ordem alfabetica: ', end ='')
# for c in sorted(times):
#     print(c, end =' ')
# print()
# print('=-'*40)

# print(f'O {times[7]} esta na 8° posicao')
