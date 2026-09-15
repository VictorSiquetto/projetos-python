# Exercício 53 – Detector de Palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()
split = frase.split()
junto = ''.join(split)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
if inverso == frase:
    print('Palindromo')
else:
    print('Nao Palindromo')
