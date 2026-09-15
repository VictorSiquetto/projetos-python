def titulo(txt):
    print('--'*15)
    print(f'{txt:^30}')
    print('--'*15)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor digite um numero inteiro valido\033[0m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mERRO: usuario preferiu nao digitar esse numero\033[0m')
            return 0
        else:
            return n

def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"\033[34m{c} - {item}\033[0m")
        c += 1
    print('--'*15)
    opc = leiaInt('\033[32mSua Opcao: \033[0m')
    return opc
