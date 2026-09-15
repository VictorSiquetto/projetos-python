# Exercício 101 – Funções para votação

def voto(n):
    from datetime import date
    atual = date.today().year
    anos = atual - n
    if anos < 16:
        return f'Com {anos} anos: Voto Negado'
    elif 18 > anos >= 16 or anos > 70:
        return f'Com {anos} anos: Voto Opcional'
    else:
        return f'Com {anos} anos: Voto Obrigatorio'

print('=-'*18)
print(voto(n = int(input('Digite o seu anos de nascimento: '))))
