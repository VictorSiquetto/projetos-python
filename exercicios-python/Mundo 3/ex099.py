# Exercício 99 – Função que descobre o maior

from time import sleep

def maior(*valores):
    print('=-'*17)
    print('Analisando os valores passados...')
    for c in valores:
        print(c, end =' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor foi {max(valores, default=0)}')


maior(2, 8, 4, 3, 5, 4, 3)
maior(4, 7, 0, 2)
maior(5, 7)
maior(6)
maior()
