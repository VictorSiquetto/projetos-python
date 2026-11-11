from crud import *


def exibir_menu():
    print("\n" + "=" * 30)
    print("     SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)


def main():

    if not criar_banco():
        print("Houve um problema ao criar o banco")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        match opcao:
            case "1":
                if not cadastrar_pessoa():
                    print("\nERRO: Nao foi possivel cadastrar a pessoa")

            case "2":
                if not listar_pessoas():
                    print("\nERRO: Nao foi possivel listar as pessoas")

            case "3":
                if not atualizar_pessoa():
                    print("\nERRO: Nao foi possivel atualizar a pessoa")

            case "4":
                if not excluir_pessoa():
                    print("\nERRO: Nao foi possivel excluir a pessoa")

            case "5":
                if not buscar_pessoa_por_nome():
                    print("\nERRO: Nao foi possivel buscar o nome da pessoa")

            case "0":
                print("\nEncerrando o sistema...")
                break

            case _:
                print("\nERRO: Opcao invalida, escolha entre 0 e 5")

        input("Pressione ENTER para continuar")


if __name__ == "__main__":
    main()
