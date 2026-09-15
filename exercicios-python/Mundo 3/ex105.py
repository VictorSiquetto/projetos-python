# Exercício 105 – Analisando e gerando Dicionários

def notas(*num, sit=False):
    lista = list(num)
    dic = {}
    dic['total'] = len(lista)
    dic['maior'] = max(lista)
    dic['menor'] = min(lista)
    media = sum(lista) / len(lista)
    dic['media'] = round(media, 2)
    if sit:
        if media >= 7:
            dic['situacao'] = 'Boa'
        elif media <= 5:
            dic['situacao'] = 'Ruim'
        else:
            dic['situacao'] = 'Razoavel'
    return dic

resp = notas(5.56, 2.53, 7.3, sit=True)
print(resp)
