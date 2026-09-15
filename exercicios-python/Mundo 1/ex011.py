# Exercício 11 – Pintando Parede

largura = float(input('Quanto de largura tem a parede: '))
altura = float(input('Quanto de altura tem a parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem {largura:.2f}m de largura, {altura:.2f}m de altura, sua area é de {area:.2f}m² e para pintá-la você precisará de {tinta:.2f} litros de tinta.')
