# Exercício 64 – Tratando vários valores v1.0

num = total = c =0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    total += num
    c += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou {c} numeros e a soma deu {total}')
