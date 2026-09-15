# UMC - Software Básico
# Victor Siquetto Vieira da Silva 
# Entrada 
import os
linha = '=' * 150
Titulo="""
██╗   ██╗ █████╗ ██╗      ██████╗ ██████╗     ██████╗  █████╗     ██████╗ ██╗ █████╗ ██████╗ ██╗ █████╗ 
██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗    ██╔══██╗██╔══██╗    ██╔══██╗██║██╔══██╗██╔══██╗██║██╔══██╗
██║   ██║███████║██║     ██║   ██║██████╔╝    ██║  ██║███████║    ██║  ██║██║███████║██████╔╝██║███████║
╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══██╗    ██║  ██║██╔══██║    ██║  ██║██║██╔══██║██╔══██╗██║██╔══██║
 ╚████╔╝ ██║  ██║███████╗╚██████╔╝██║  ██║    ██████╔╝██║  ██║    ██████╔╝██║██║  ██║██║  ██║██║██║  ██║
  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
"""
# Processamento
while True:
    os.system("cls")
    print(linha)
    print ("\033[1;34m",Titulo,"\033[0;m")
    try:
       print('''
               Quantidade de Pessoas       Diária          Diária
                   no Apartamento         tipo 1(R$)      tipo2 (R$)
	                1                  20,00           25,00	
	                2                  28,00           34,00
	                3                  35,00           42,00
	                4                  42,00           50,00
	                5                  48,00           57,00
	                6                  53,00           63,00
             ''')
       nome=(input("Qual o seu nome: "))
       cpf=int(input("Qual o seu CPF: "))
       tipo=int(input("Qual o seu tipo de apartamento (1 ou 2): "))
       if tipo != 1 and tipo != 2:
           print(f"{"\033[1;31m"}Opção inválida, escolha entre 1 ou 2.{"\033[0;m"}")
       else:
           dias=int(input("Quantidade de dias no apartamento: "))
           if dias == ValueError:
               print(f"{"\033[1;31m"}Entrada inválida, insira um número válido.{"\033[0;m"}")
           else:
               pessoas=int(input("Quantidade de pessoas no apartamento (1 a 6): "))
               if pessoas < 1 or pessoas > 6:
                   print(f"{"\033[1;31m"}Opção inválida, escolha entre 1 a 6.{"\033[0;m"}")
               else:
                   tabela_precos = {
                        1: {1: 20.00, 2: 25.00},
                        2: {1: 28.00, 2: 34.00},
                        3: {1: 35.00, 2: 42.00},
                        4: {1: 42.00, 2: 50.00},
                        5: {1: 48.00, 2: 57.00},
                        6: {1: 53.00, 2: 63.00},
                    }
# Saída                   
                   total = tabela_precos[pessoas][tipo] 
                   print(f"Bem-Vindo {"\033[1;32m"}{nome} - {cpf}{"\033[0;m"}, o seu tipo de apartamento é {"\033[1;32m"}{tipo}{"\033[0;m"}, você ficará por {"\033[1;32m"}{dias}{"\033[0;m"} dia(s), o número de pessoas é {"\033[1;32m"}{pessoas}{"\033[0;m"} e o preço total será de: {"\033[1;32m"} R$ {total*dias:.2f} {"\033[0;m"}")
                   print(linha)
    except ValueError:
        print(f"{"\033[1;31m"}Entrada inválida, insira um número válido.{"\033[0;m"}")
    opt = input("Pressione Enter para continuar ou F para finalizar: ")
    if opt == "f" or opt == "F":
        break
print("Programa Finalizado")
