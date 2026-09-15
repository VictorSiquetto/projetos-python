# Exercício 67 – Tabuada v3.0

c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    while c < 11:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
    c = 1
print('Programa finalizado')

# for c in range(1, 11):              Tira a necessidade do contador c = 1
#     print(f'{n} x {c:2} = {n*c}') 