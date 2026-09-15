# Exercício 56 – Analisador completo

soma = 0
mais_velho = ''
maior_idade = 0
mulheres_menos_de_20 = 0
for c in range(1,5):
    print(f'--- {c}° Pessoa ---')
    nome = str(input('Qual seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo M/F: ')).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        mais_velho = nome
        maior_idade = idade
    if sexo == 'M' and idade > maior_idade:
            mais_velho = nome
            maior_idade = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1
media = soma / 4
print(f'A media de idade é de {media:.2f} anos')
print(f'O homem mais velho é {mais_velho} e ele tem {maior_idade} anos')
print(f'E temos {mulheres_menos_de_20} mulheres com menos de 20 anos')
