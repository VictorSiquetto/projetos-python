# Exercício 12 – Calculando Descontos

preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 5 / 100
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco - desconto:.2f}.')
