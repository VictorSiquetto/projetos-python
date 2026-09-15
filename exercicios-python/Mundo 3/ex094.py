# Exercício 94 – Unindo dicionários e listas

dic = {}
lista = []
mulheres = []
tot = 0
while True:
    dic.clear()
    dic['nome'] = str(input('Nome: '))
    dic['sexo'] = ' '
    while dic['sexo'] not in 'MF':
        dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dic['sexo'] not in 'MF':
            print('Erro, digite apenas M ou F')
        if dic['sexo'] == 'F':
            mulheres.append(dic['nome'])
    dic['idade'] = int(input('Idade: '))
    tot += dic['idade']
    lista.append(dic.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Erro, digite apenas S ou N')
    if opcao == 'N':
        break
media = tot / (len(lista))
print('=-'*20)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A media de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram', end =' ')
for m in mulheres:
    print(m, end =' ')
print('\nLista das pessoas que estao acima da media: ')
for c in lista:
    if c['idade'] > media:
        print(f"Nome = {c['nome']}; Sexo = {c['sexo']}; Idade = {c['idade']}")
print('Encerrado')

# dic = {}
# lista = []
# tot = 0
# while True:
#     dic.clear()
#     dic['nome'] = str(input('Nome: '))
#     while True:
#         dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
#         if dic['sexo'] in 'MF':
#             break
#         print('Erro, digite apenas M ou F')
#     dic['idade'] = int(input('Idade: '))
#     tot += dic['idade']
#     lista.append(dic.copy())
#     while True:
#         opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
#         if opcao in 'SN':
#             break
#         print('Erro, digite apenas S ou N')
#     if opcao == 'N':
#         break
# media = tot / (len(lista))
# print('=-'*20)
# print(f'Ao todo temos {len(lista)} pessoas cadastradas')
# print(f'A media de idade é de {media:.2f} anos')
# print('As mulheres cadastradas foram', end =' ')
# for m in lista:
#     if m['sexo'] in 'Ff':
#         print(m['nome'], end =' ')
# print()
# print('Lista das pessoas que estao acima da media: ')
# for c in lista:
#     if c['idade'] > media:
#         for k, v in c.items():
#             print(f'{k} = {v}; ', end = '')
#         print()
# print('Encerrado')