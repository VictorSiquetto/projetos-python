# Exercício 96 – Função que calcula área

def area(comp, larg):
    area = comp * larg
    print(f'A area de {comp:.2f} x {larg:.2f} é {area:.2f}m²')

print('Controle de Terrenos')
print('--'*10)
comp = float(input('Digite o comprimento (m): '))
larg = float(input('Digite a largura (m): '))
area(comp, larg)
