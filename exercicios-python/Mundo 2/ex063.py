# Exercício 63 – Sequência de Fibonacci v1.0

num = int(input('Quantos termos voce quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end ='')
while c <= num:
    t3 = t1 + t2
    print(t3, '-> ', end ='')
    t1 = t2
    t2 = t3
    c += 1
print('Fim')
