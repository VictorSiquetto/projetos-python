# Exercício 72 – Número por Extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    teclado = int(input('Digite um numero de 0 a 20: '))
    if teclado > 20 or teclado < 0:
        print('Tente novamente')
    else:
        break
print(f'Voce digitou o numero {numeros[teclado]}')
