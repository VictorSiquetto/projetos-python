# Exercício 62 – Super Progressão Aritmética v3.0

p = int(input('Qual o primeiro numero da PA: '))
r = int(input('Qual a razao da PA: '))
c = 1
mais = 10
while mais != 0:
    mais += c - 1
    while c <= mais:
        print(f'{p} -> ', end ='')
        p += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Progresso finalizado com {c - 1} termos mostrados')
