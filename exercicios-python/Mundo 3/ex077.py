# Exercício 77 – Contando vogais em Tupla

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end ='')
    for vogais in c:
        if vogais.lower() in 'aeiou':
            print(vogais, end =' ')
