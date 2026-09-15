# Exercício 34 – Aumentos múltiplos

salario = float(input('Digite o salario do funcionario: R$'))
if salario > 1250.00:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)
print(f'Seu novo salario sera de R${aumento:.2f}')
