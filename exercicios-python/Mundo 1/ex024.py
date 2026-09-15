# Exercício 24 – Verificando as primeiras letras de um texto

cid = str(input('Em qual cidade voce nasceu: ')).strip().upper()
print(f'Voce nasceu em Santo? {cid[:5] == 'SANTO'}')
