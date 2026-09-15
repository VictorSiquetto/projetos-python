# Exercício 59 – Criando um Menu de Opções

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos numeros\n[ 5 ] Sair do programa')
    opcao = int(input('Qual a sua opcao: '))
    if opcao == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}')
    elif opcao == 2:
        print(f'A multiplicacao de {num1} e {num2} é {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior numero é {num1}')
        elif num2 > num1:
            print(f'O maior numero é {num2}')
        else:
            print(f'Os numeros sao iguais')
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Voce saiu do programa')
    else:
        print('Digite um numero valido')
print('Fim')
