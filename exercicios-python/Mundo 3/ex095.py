# Exercício 95 – Aprimorando os Dicionários

jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Erro, digite apenas S ou N')
    if opcao == 'N':
        break
print('=-'*20)
print(f'{'cod':<5}', end =' ')
for i in jogador.keys():
    print(f'{i:<15}', end ='')
print()
print('--'*20)
for pos, i in enumerate(time):
    print(f'{pos:<5}', end =' ')
    for v in i.values():
        print(f'{str(v):<15}', end ='')
    print()
while True:
    while True:
        print('--'*20)
        dados = int(input('Mostrar dados de qual jogador (999 para parar): '))
        if dados <= len(time) - 1:
            print(f' -- Levantamento de dados do jogador {time[dados]['nome']}:')
            for p, g in enumerate(time[dados]['gols']):
                print(f'   => Na partida {p}, fez {g} gols')
        if dados == 999:
            print('Volte sempre')
            break
        if dados > len(time) - 1:
            print(f'Erro, nao existe jogador com o codigo {dados}')
    break
