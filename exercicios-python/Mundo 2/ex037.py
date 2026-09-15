# Exercício 37 – Conversor de Bases Numéricas

numero = int(input('Qual o numero: '))

print('Escolha sua conversao \n 1 para binario \n 2 para octal \n 3 para hexadecimal')

escolha = int(input('Qual sua escolha: '))

if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero)[2:])
elif escolha == 3:
    print(hex(numero)[2:])
else:
    print('Escolha um numero valido')
