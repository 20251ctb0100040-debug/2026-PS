catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": False},
    {"titulo": "Padrões de Projeto", "autor": "Erich Gamma", "disponivel": True},
]

def listar_livros():
    print("\n" + "=" * 50)
    print("📚 CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print(" Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponivel" if livro["disponivel"] else "❌ Emprestado"
        print(f"    {i}. {livro['titulo']} - {livro['autor']} [{status}]")
    print("=" * 50)

def adicionar_livro():
    print("\n---- Adicionar Novo Livro ----")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if not titulo or not autor:
        print("⚠️ Titulo e autor são obrigatorios.")
        return
    
    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })
    print(f"✅ '{titulo}' adicionado com sucesso!")

def buscar_livro():
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()

    resultados = [livro for livro in catalogo if termo in livro["titulo"].lower()]

    if not resultados:
        print("  Nenhum livro encontrado.")
        return

    print(f"\n({len(resultados)}) resultado(s):")
    for livro in resultados:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f" • {livro['titulo']} - {livro['autor']} [{status}]")

def registrar_emprestimo():
    listar_livros()
    if not catalogo: return
        
    print("\n--- Registrar Empréstimo ---")
    try:
        numero = int(input("Número do livro: ")) 
        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return
            
        livro = catalogo[numero - 1] 
        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f"✅ Empréstimo de '{livro['titulo']}' registrado.")
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")

def devolver_livro():
    listar_livros()
    if not catalogo: return
    
    print("\n--- Registrar Devolução ---")
    try:
        numero = int(input("Número do livro a devolver: "))
        if numero < 1 or numero > len(catalogo):
            print("❌ Número fora da lista.")
            return

        livro = catalogo[numero - 1]
        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"✅ Devolução de '{livro['titulo']}' registrada.")
    except ValueError:
        print("❌ Digite apenas o número do livro.")

def menu():
    print("\n SISTEMA DE BIBLIOTECA - v1 (em memória)")
    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro", devolver_livro),
        "0": ("Sair", None),
    }

    while True:
        print("\n Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f" [{chave}] {descricao}")

        try:
            escolha = input("\n Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
        except ValueError as e:
            print(f"⚠️ {e}")
            continue
        else:
            if escolha == "0":
                print("\n Até logo! 👋")
                break
            _, funcao = opcoes[escolha]
            funcao()

if __name__ == "__main__":
    menu()
