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

#---- listas: CONCEIOS BÁSICOS ----

# Criando uma lista de titulos

titulos = [
    "O Programador Pragmático",
    "Codigo limpo",
    "Entendendo algoritmos",
]

# Acesso por indice (começa em 0, não em 1!)
print("primeiro livro:", titulos[0])
print("Último livro :", titulos[-1]) #indice -1 = último elemento
print("Total de livros:", len(titulos))

# ---- METODOS  DE LISTAS ----

print("\n--- Operações na lista ---")

#Adicionar um item ao final

titulos.append("Python fluente")
print("Após append:", titulos)

# Verificar se um item existe

busca = "Codigo limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')
else:
    print(f'"{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()

print("Lista ordenada:", titulos)

# Remover um item
if "Entendendo algoritmos" in titulos:
    titulos.remove("Entendendo algoritmos")

print("Após remove:")
for i, titulo in enumerate(titulos,1):
    print(f"{i}. {titulo}")

# Um dicionário representa um livro com seus atributos
livro = {
    "titulo":       "O Programador Pragmático",
    "autor":        "Andrew Hunt",
    "ano":          1999,               #int, não string
    "disponivel":  True,                #bool    
}

# acessando valores pela chaves

print("Título :", livro["titulo"])
print("Autor :", livro["autor"])
print("Ano  :",  livro["ano"])
print("Statu :", "Disponível" if livro["disponivel"] else "Emprestado")

#---- MODIFICANDO E CONULTANDO ----

# Atualizando um valor existente
livro["disponivel"] = False     #livro foi emprestado
print("\nApós emprestimo:", livro["disponivel"])

# Adicionando uma nova chave
livro["paginas"] = 352
print("Páginas:", livro["paginas"])

# .get()- acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora:", editora)      # não lança KeyError, retorna o padrão

#---- CATALOGO LISTA DE DICIONARIOS ----

catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999,
"disponivel": True},
    {"titulo": "Código limpo", "autor":  "Robert C. Martin", "ano": 2008,
"disponivel": False},
{"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
"disponivel": True},
{"titulo": "Python Fluente", "autor": "Luciano Ramalho", "ano": 2015,
"disponivel": True }
]

print("=== Ctálogo da Biblioteca ===")
print()

# Percorrendo cada livro com for 

for i, livro in enumerate(catalogo, 1):
    status = " Diponivel" if livro["disponivel"] else "Emprestado"
    print(f'    {i}. {livro["titulo"]} ({livro["ano"]})')
    print(f'    Autor:  {livro["autor"]} {status}')
    print("  "+ "-" * 40)

# ---- CONSULTS E FITROS ----

print("\n=== Livros dispoíveis ===")
for livro in catalogo:
    if livro["disponivel"]:     #filtra apenas os disponiveis
        print(f'    certo: {livro["titulo"]}')

print("\n=== Busca por titulo ===")
busca = input("Digite o titulos (ou parte): ").lower()
encontrado = False
for livro in catalogo:
    if busca in livro["titulo"].lower(): #.lower ignora maiusculos/minusculas
        print(f'    Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True

if not encontrado:
    print(" Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():
    print(f"    {chave}: {valor}")
