# Exercício 97 – Um print especial

def escreva(frase):
    tam = len(frase) + 4
    print('='*tam)
    print(f'  {frase}')
    print('='*tam)

escreva('Victor')
escreva('Curso de Python')
escreva('Oi')
