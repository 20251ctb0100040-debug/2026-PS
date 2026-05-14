'''
=====================================================
# ARQUIVO : hotel pets v2
# Disciplina : Programação de Sistemas (2026-2)
# Aula : Aula 20 - Por que POO?
# Autor: Luis Gustavo Pereira
# Conceitos :Classe, objeto, atributos, métodos, encapsulamento
#Atividade : Classe Pet
=====================================================
'''
import pickle


class Pet:
    """
    Representa um pet no sistema do hotel.
    """

    def __init__(self, nome, especie, idade, raca, peso,
                 nome_dono, telefone_dono, vacinado, observacoes):

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.peso = peso
        self.nome_dono = nome_dono
        self.telefone_dono = telefone_dono
        self.vacinado = vacinado.lower()
        self.observacoes = observacoes
        self.hospedado = False

    def exibir_dados(self):
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Telefone: {self.telefone_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado == 'sim' else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Observações: {self.observacoes}")

    def registro_entrada(self):
        if self.hospedado:
            print(f"{self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registro_saida(self):
        if not self.hospedado:
            print(f"{self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        if self.idade <= 3:
            return 50
        elif self.idade <= 10:
            return 60
        else:
            return 75

    def emitir_resumo(self):
        valor = self.calcular_diaria()

        return (
            f"\nNome: {self.nome}\n"
            f"Espécie: {self.especie}\n"
            f"Diária: R$ {valor:.2f}\n"
            f"Hospedado: {'Sim' if self.hospedado else 'Não'}"
        )

    def para_linha_txt(self):
        return (
            f"{self.nome};{self.especie};{self.idade};"
            f"{self.raca};{self.peso};{self.nome_dono};"
            f"{self.telefone_dono};{self.vacinado};"
            f"{self.observacoes};{self.hospedado}"
        )


# =====================================================
# PERSISTÊNCIA
# =====================================================

def salvar_em_txt(pets, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for pet in pets:
            arquivo.write(pet.para_linha_txt() + "\n")

    print(f"\n✅ {len(pets)} pet(s) salvo(s) em {caminho}")


def salvar_em_binario(pets, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(pets, arquivo)

    print(f"\n✅ {len(pets)} pet(s) salvo(s) em {caminho}")


def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)

    except FileNotFoundError:
        print("Arquivo não encontrado. Sistema iniciado vazio.")
        return []


# =====================================================
# FUNÇÕES DO SISTEMA
# =====================================================

def cadastrar_pet(pets):

    print("\n===== Cadastro de Pet =====")

    nome = input("Nome: ")
    especie = input("Espécie: ")

    idade = int(input("Idade: "))

    raca = input("Raça: ")

    peso = float(input("Peso: "))

    nome_dono = input("Nome do dono: ")

    telefone_dono = input("Telefone do dono: ")

    vacinado = input("Vacinado (sim/não): ")

    observacoes = input("Observações: ")

    novo_pet = Pet(
        nome,
        especie,
        idade,
        raca,
        peso,
        nome_dono,
        telefone_dono,
        vacinado,
        observacoes
    )

    pets.append(novo_pet)

    print("\n✅ Pet cadastrado com sucesso.")


def listar_pets(pets):

    if not pets:
        print("\nNenhum pet cadastrado.")
        return

    print(f"\n===== Lista de Pets ({len(pets)}) =====")

    for i, pet in enumerate(pets, start=1):

        print(f"\n[{i}]")
        pet.exibir_dados()


def entrada_pet(pets):

    listar_pets(pets)

    if not pets:
        return

    try:
        indice = int(input("\nNúmero do pet: ")) - 1

        if 0 <= indice < len(pets):
            pets[indice].registro_entrada()
        else:
            print("Índice inválido.")

    except ValueError:
        print("Digite um número válido.")


def saida_pet(pets):

    listar_pets(pets)

    if not pets:
        return

    try:
        indice = int(input("\nNúmero do pet: ")) - 1

        if 0 <= indice < len(pets):
            pets[indice].registro_saida()
        else:
            print("Índice inválido.")

    except ValueError:
        print("Digite um número válido.")


def resumo_pet(pets):

    listar_pets(pets)

    if not pets:
        return

    try:
        indice = int(input("\nNúmero do pet: ")) - 1

        if 0 <= indice < len(pets):
            print(pets[indice].emitir_resumo())
        else:
            print("Índice inválido.")

    except ValueError:
        print("Digite um número válido.")


# =====================================================
# MENU
# =====================================================

def menu():

    pets = carregar_de_binario("pets.bin")

    while True:

        print("\n========== HOTEL PET ==========")
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Emitir resumo")
        print("6 - Salvar em TXT")
        print("7 - Salvar em Binário")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_pet(pets)

        elif opcao == "2":
            listar_pets(pets)

        elif opcao == "3":
            entrada_pet(pets)

        elif opcao == "4":
            saida_pet(pets)

        elif opcao == "5":
            resumo_pet(pets)

        elif opcao == "6":
            salvar_em_txt(pets, "pets.txt")

        elif opcao == "7":
            salvar_em_binario(pets, "pets.bin")

        elif opcao == "0":

            salvar_em_binario(pets, "pets.bin")

            print("\nAté logo.")
            break

        else:
            print("Opção inválida.")


# =====================================================
# EXECUÇÃO
# =====================================================

if __name__ == "__main__":
    menu()