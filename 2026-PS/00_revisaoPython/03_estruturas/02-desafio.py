# ===================================================
#lista e dicionarios
#====================================================
#Disciplina : Programação de Sistmas (PS)
# Aula      : 05 - Revisão: Etruturas e dados: listas e dicionarios
# Autor     : [Luis Gustavo Pereira Melo]
#Data       : [12/03/2026]
# Repositorio:  https://github.com
#====================================================
#
# DISCRIÇÃO
# Catálogo de livros que demonstra o uso de listas 
# e dicionarios para armazenar, conultar e filtrar
# dados estruturados.
#====================================================

# Lista de livros
lista_livros = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acessando itens da lista
print("Primeiro livro:", lista_livros[0])
print("Último livro  :", lista_livros[-1])  # -1 pega o último
print("Total de livros:", len(lista_livros))  # tamanho da lista


# ================================================
# OPERAÇÕES NA LISTA
# ================================================

print("\n--- Operações na lista ---")

# Adiciona um livro
lista_livros.append("Python Fluente")
print("Após append:", lista_livros)

# Verifica se existe
livro_busca = "Código Limpo"
if livro_busca in lista_livros:
    print(f'"{livro_busca}" está no catálogo.')
else:
    print(f'"{livro_busca}" não encontrado.')

# Ordena a lista
lista_livros.sort()
print("Lista ordenada:", lista_livros)

# Remove um livro
lista_livros.remove("Entendendo Algoritmos")
print("Após remove:", lista_livros)


# ================================================
# DICIONÁRIO
# ================================================

# Dicionário de um livro
item_livro = {
    "titulo": "O Programador Pragmático",
    "autor": "Andrew Hunt",
    "ano": 1999,
    "disponivel": True,
}

# Acessa valores pelas chaves
print("Titulo :", item_livro["titulo"])
print("Autor  :", item_livro["autor"])
print("Ano    :", item_livro["ano"])

# Mostra status
print("Status :", "Disponível" if item_livro["disponivel"] else "Emprestado")


# ================================================
# ALTERAÇÃO DE DADOS
# ================================================

# Marca como emprestado
item_livro["disponivel"] = False

# .get evita erro se chave não existir
print("Páginas:", item_livro.get("paginas", "Não informado"))

# Outro uso do .get
editora_livro = item_livro.get("editora", "Não informado")
print("Editora:", editora_livro)


# ================================================
# CATÁLOGO
# ================================================

# Lista de dicionários (livros)
biblioteca = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2017, "disponivel": False},
]

print("\n=== Catálogo da Biblioteca ===")
print()

# Percorre todos os livros
for item_livro in biblioteca:
    situacao = "Disponível" if item_livro["disponivel"] else "Emprestado"
    print(f'     {item_livro["titulo"]} ({item_livro["ano"]})')
    print(f'     Autor: {item_livro["autor"]} | {situacao}')
    print("  " + "-" * 40)


# ================================================
# FILTRO DE LIVROS
# ================================================

print("\n=== Livros disponíveis ===")

# Mostra apenas disponíveis
for item_livro in biblioteca:
    if item_livro["disponivel"]:
        print(f'    {item_livro["titulo"]}')

print("\n=== Busca por título ===")

# Usuário digita parte do título
texto_busca = input("Digite o título (ou parte): ").lower()
achou = False

# Procura no catálogo
for item_livro in biblioteca:
    if texto_busca in item_livro["titulo"].lower():
        print(f'  Encontrado: {item_livro["titulo"]} - {item_livro["autor"]}')
        achou = True

# Caso não encontre
if not achou:
    print("  Nenhum livro encontrado.")


# ================================================
# ATRIBUTOS DO PRIMEIRO LIVRO
# ================================================

print("\n=== Atributos do primeiro livro ===")

# Mostra chave e valor
for chave, valor in biblioteca[0].items():
    print(f"   {chave}: {valor}")


# ================================================
# CADASTRO DE LIVRO
# ================================================

print("\n=== Cadastro de novo livro ===")

# Entrada de dados
novo_titulo = input("Título do livro: ")
novo_autor = input("Autor do livro: ")
novo_ano = int(input("Ano de publicação: "))

# Cria novo livro
livro_novo = {
    "titulo": novo_titulo,
    "autor": novo_autor,
    "ano": novo_ano,
    "disponivel": True
}

# Adiciona ao catálogo
biblioteca.append(livro_novo)

print("\n=== Catálogo atualizado ===")

# Mostra catálogo novamente
for item_livro in biblioteca:
    situacao = "Disponível" if item_livro["disponivel"] else "Emprestado"
    print(f'     {item_livro["titulo"]} ({item_livro["ano"]})')
    print(f'     Autor: {item_livro["autor"]} | {situacao}')
    print("  " + "-" * 40)


# ================================================
# BUSCA POR AUTOR
# ================================================

print("\n=== Busca por autor ===")

# Usuário digita o autor
busca_autor = input("Digite o autor: ").lower()
achou = False

# Procura livros do autor
for item_livro in biblioteca:
    if busca_autor in item_livro["autor"].lower():
        situacao = "Disponível" if item_livro["disponivel"] else "Emprestado"
        print(f'  {item_livro["titulo"]} - {item_livro["autor"]} | {situacao}')
        achou = True

# Caso não encontre
if not achou:
    print("  Nenhum livro encontrado.")


# ================================================
# EMPRÉSTIMO / DEVOLUÇÃO
# ================================================

print("\n=== Empréstimo / devolução ===")

# Usuário digita o título
titulo_alterar = input("Digite o título do livro: ").lower()
achou = False

# Procura e altera status
for item_livro in biblioteca:
    if titulo_alterar in item_livro["titulo"].lower():

        # alterna True/False
        item_livro["disponivel"] = not item_livro["disponivel"]

        situacao = "Disponível" if item_livro["disponivel"] else "Emprestado"
        print(f'  Status atualizado: {item_livro["titulo"]} agora está {situacao}')
        achou = True

# Caso não encontre
if not achou:
    print("  Livro não encontrado.")


# ================================================
# RELATÓRIO FINAL
# ================================================

print("\n=== Relatório final ===")

# Calcula totais
total_livros = len(biblioteca)
qtd_disponivel = 0
qtd_emprestado = 0

# Conta disponíveis e emprestados
for item_livro in biblioteca:
    if item_livro["disponivel"]:
        qtd_disponivel += 1
    else:
        qtd_emprestado += 1

print("Total de livros :", total_livros)
print("Disponíveis     :", qtd_disponivel)
print("Emprestados     :", qtd_emprestado)

print("\nLivros emprestados:")

# Lista os emprestados
for item_livro in biblioteca:
    if not item_livro["disponivel"]:
        print(" -", item_livro["titulo"])