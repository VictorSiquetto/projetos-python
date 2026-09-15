# Exercício 93 – Cadastro de Jogador de Futebol

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
print('=-'*20)
print(jogador)
print('=-'*20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*20)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas')   # ao inves de {partidas} poderia ser {len(jogador['gols'])}
for p, g in enumerate(gols):
    print(f' => Na partida {p}, fez {g} gols')
print(f'Foi um total de {jogador['total']} gols')
