"""
agenda.py - Aula 23 (Programação de sistemas, 2026)
Agenda de Contatos com menu interativo e persistencia (.txt e binário)
"""
import pickle

class Contato:
    """Representa um contato da agenda."""

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def exibir(self):
        print(f" Nome : {self.nome}")
        print(f" Telefone: {self.telefone}")
        print(f" Email: {self.email}")
    
    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"
    

def salvar_em_txt(contatos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            arquivo.write(c.para_linha_txt() + "\n")
    print(f"✅ {len(contatos)} contato(s) salvo(s) em {caminho}")


def carregar_de_txt(caminho):
    """Lê o arquivo de texto e RECONSTROI os objetos Contato"""
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
    return contatos


def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"✅ {len(contatos)} contato(s) salvo(s) em {caminho}")


def carregar_de_binario(caminho):
    """Lê o arquivo binário e devolve a lista de objetos pronta."""
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não exite. Começando vazio.")
        return []
    

def cadastrar(contatos):
    """Lê os dados via input e adiciona um novo Contato na lista."""
    print("\n--- Novo contato ---")
    nome = input("Nome   :")
    telefone = input("Telefone: ")
    email = input("Email :")
    contatos.append(Contato(nome, telefone, email))
    print("✅ Contato cadastrado.")


def listar(contatos):
    """Mostra todos os contatos cadastrados, numerados."""
    if not contatos:
        # Caso especial: lista vazia. Sempre tratamos antes de iterar.
        print("\n(agenda vazia)")
        return

    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    # enumerate(start=1) numera começando em 1 (mais amigável que 0
    # para o usuário final, que não pensa "índice" — pensa "posição").
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]")
        # Cada Contato sabe se exibir — chamamos o método.
        c.exibir()


def remover(contatos):
    """Mostra a lista, pede um número e remove o contato escolhido."""
    listar(contatos)
    if not contatos:
        return

    # int(input(...)) converte texto para número. Cuidado: se o usuário
    # digitar uma letra, dá ValueError. Para um sistema mais robusto,
    # envolveríamos em try/except — fica como exercício.
    indice = int(input("\nNº do contato a remover: ")) - 1
    # Validação: o índice precisa estar dentro dos limites da lista.
    if 0 <= indice < len(contatos):
        # pop(indice) remove e retorna o elemento naquela posição.
        removido = contatos.pop(indice)
        print(f"✓ Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")


def menu():
    # Carregamos o estado salvo da execução anterior (se existir).
    # Escolhemos o formato binário porque preserva os objetos intactos.
    contatos = carregar_de_binario("agenda.bin")

    while True:  # loop infinito — só sai com break (opção 0).
        print("\n========== AGENDA ==========")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Salvar em .txt")
        print("5 - Salvar em binário")
        print("0 - Sair")
        opcao = input("Opção: ")

        # Despacho por opção. Cada caso chama uma função especializada
        # — o menu não sabe NADA sobre como cadastrar, listar etc.
        # Essa separação entre "interface" e "lógica" é o que permite
        # trocar o menu por uma GUI no futuro sem reescrever o sistema.
        if opcao == "1":
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_txt(contatos, "agenda.txt")
        elif opcao == "5":
            salvar_em_binario(contatos, "agenda.bin")
        elif opcao == "0":
            # Antes de sair, salvamos automaticamente. Garantia de
            # que o usuário não perde o trabalho da sessão.
            salvar_em_binario(contatos, "agenda.bin")
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()