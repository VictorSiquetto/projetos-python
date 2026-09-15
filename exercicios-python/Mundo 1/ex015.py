# Exercício 15 – Aluguel de Carros

km = float(input('Quantos Km foram percorridos: '))
dias = int(input('Quantos dias o carro foi alugado: '))
preco = dias * 60 + km * 0.15
print(f'O total a pagar pelo aluguel do carro é de R${preco:.2f}.')
