# Exercício 43 – Índice de Massa Corporal

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / altura**2
print(f'o imc é de {imc:.2f}, ', end='')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')
