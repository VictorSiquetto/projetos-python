# Exercício 60 – Cálculo do Fatorial

num = int(input('Digite um numero para saber seu fatorial: '))
c = num
f = 1
while c > 0:
    print(c, end ='')
    print(' x ' if c > 1 else ' = ', end ='')
    f *= c
    c -= 1
print(f)    
