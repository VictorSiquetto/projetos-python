def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! "{n}" é um preço invalido\033[0m') 
        else:
            ok = True
            return float(n)