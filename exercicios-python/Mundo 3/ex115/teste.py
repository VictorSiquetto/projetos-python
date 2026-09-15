from modulos.interface.funcoes import *
from modulos.arquivo.arquivo import *
from time import sleep

arq = 'Exercicios-Python\\Mundo 3\\ex115\\cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        titulo('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        titulo('Saindo do Programa')
        break
    else:
        print(f'\033[31mERRO: por favor digite uma opcao valida\033[0m')
    sleep(2)
