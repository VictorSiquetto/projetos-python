# Exercício 78 – Maior e Menor valores na Lista

lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    lista.append(num)
for pos, c in enumerate(lista):
    if c == max(lista):
        print(f'O maior numero é {c} e esta na posciao {pos+1}')
    if c == min(lista):
        print(f'O menor numero é {c} e esta na posciao {pos+1}')
