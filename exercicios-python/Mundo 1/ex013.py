# Exercício 13 – Reajuste Salarial

salario = float(input('Digite o salario do funcionario: R$'))
reajuste = salario * 15 / 100
print(f'O funcionario que ganhava R${salario:.2f}, com o reajuste de 15% vai passar a ganhar R${salario + reajuste:.2f}.')
