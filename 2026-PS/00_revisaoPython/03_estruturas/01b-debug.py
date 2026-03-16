# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

# O índice 3 não existe, pois a lista possui apenas as posições 0, 1 e 2.
print("Primeiro livro:", catalogo[2]["titulo"])

print("\nLivros disponíveis:")

for livro in catalogo:
# A condição está verificando == False, mas o exercício pede para mostrar os livros disponíveis (True).
    if livro["disponivel"] == True:
        print(f"  {livro['titulo']}")

total = len(catalogo)
print(f"\nTotal de livros: {total}")

# Faltou utilizar .items() para percorrer as chaves e os valores do dicionário.
for chave, valor in catalogo[0].items():
    print(f"  {chave}: {valor}")

# A chave foi utilizada com letra maiúscula, porém foi definida em minúsculo.
primeiro_autor = catalogo[0]["autor"]

print("\nAutor do primeiro livro:", primeiro_autor)