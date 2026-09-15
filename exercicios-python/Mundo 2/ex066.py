# Exercício 66 – Vários números com flag

n = s = c =0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} numeros e a soma deu {s}')
