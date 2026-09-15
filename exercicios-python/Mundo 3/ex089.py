# Exercício 89 – Boletim com listas compostas

lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print('=-'*12)
print(f'{'No':<4}{'Nome':>8}{'Media':>10}')
print('=-'*12)
for pos, i in enumerate(lista):
    print(f'{pos:<4}{i[0]:>8}{i[2]:>9}')

while True:
    print('---'*15)
    notas = ' '
    while notas == ' ':
        notas = int(input('Mostrar notas de qual aluno (999 interrompe): '))
        if notas <= len(lista) - 1:
            print(f'As notas de {lista[notas][0]} sao {lista[notas][1]}')
    if notas == 999:
        print('Finalizando...')
        break
