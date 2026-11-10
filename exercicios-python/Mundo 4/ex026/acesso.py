import sqlite3
from datetime import date

busca = input("Quem voce esta procurando? ").strip()
hoje = date.today()

try:
    with sqlite3.connect("ex026/meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0
        for total, amigo in enumerate(cur, start=1):
            txtnasc = amigo["nascimento"]
            info_nasc = ""

            if not txtnasc:
                info_nasc = "sem data de nascimento"
            else:
                try:
                    data = date.fromisoformat(str(txtnasc))
                    japassou = (hoje.month, hoje.day) >= (data.month, data.day)
                    idade = hoje.year - data.year - (0 if japassou else 1)
                    info_nasc = f"nasceu em {data:%d/%m/%Y} e tem {idade} anos"
                except ValueError:
                    info_nasc = "data invalida"

            print(f"{amigo['nome']} {info_nasc}")

        print("-" * 37)
        if total == 0:
            print(f"Nao encontrei ninguem com '{busca}' no nome")
        elif total == 1:
            print(f"Encontrei apenas 1 amigo com '{busca}'")
        else:
            print(f"Ao todo encontrei {total} amigos com '{busca}'")

except sqlite3.Error as erro:
    print(f"ERRO no banco: {erro}")
except Exception as erro:
    print(f"ERRO: {erro}")
