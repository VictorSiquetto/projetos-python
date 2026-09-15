# Exercício 114 – Site está acessível?

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print(f'O google nao esta acessivel no momento')
else:
    print('Consegui acessar o google com sucesso')
