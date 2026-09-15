# Exercício 36 – Aprovando Empréstimo

valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salario: R$'))
anos = int(input('Em quantos anos vai pagar: '))

prestacao_mensal = valor_casa / (anos*12)


if prestacao_mensal > (salario/100*30):
    print('Voce excedeu os 30% portanto nao pode realizar o emprestimo')
else:
    print('Parabens emprestimo realizado') 
