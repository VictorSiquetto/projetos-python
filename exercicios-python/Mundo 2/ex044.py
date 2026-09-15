# Exercício 44 – Gerenciador de Pagamentos

preco = float(input('Qual o preço do produto? R$'))
print('''Qual sera o meio de pagamento?
1) à vista dinheiro/cheque
2) à vista no cartao
3) até 2x no cartao
4) 3x ou mais no cartao''')
opcao = int(input('Escolha o metodo: '))

if opcao == 1:
    print(f'O valor sera de R${preco - (preco*10/100):.2f}')
elif opcao == 2:
    print(f'O valor sera de R${preco - (preco*5/100):.2f}')
elif opcao == 3:
    print(f'O valor sera de R${preco:.2f} em 2x de R${preco/2:.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'O valor sera de R${preco + (preco*20/100):.2f} em {parcelas}x de R${(preco + (preco*20/100))/parcelas:.2f}')
else:
    print('Escolha uma opcao valida')
