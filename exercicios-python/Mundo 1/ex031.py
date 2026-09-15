# Exercício 31 – Custo da Viagem

km = float(input('Quantos km na viagem: '))
if km <= 200:
    total = km * 0.5
    print(f'O total a ser pago é {total:.2f}')
else:
    total = km * 0.45
    print(f'O total a ser pago é {total:.2f}')
