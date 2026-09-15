# Exercício 83 – Validando expressões matemáticas

exp = str(input('Digite a sua expressao: '))
lista = []
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressao é valida')
else:
    print('Sua expressao nao é valida')
