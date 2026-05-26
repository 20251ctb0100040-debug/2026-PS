'''
=====================================================
# ARQUIVO : hotel pets v3 (JSON + Blindagem de Erros)
# Disciplina : Programação de Sistemas (2026-2)
# Aula : Aula 20 - Por que POO?
# Autor: Luis Gustavo Pereira (Modificado)
# Conceitos : Classe, objeto, atributos, métodos, encapsulamento, JSON
# Atividade : Integração e Compatibilidade de Dados
=====================================================
'''

import json
import os

ARQUIVO_JSON = "2026-PS/02_poo/hotel_pets_json/pets.json"


class Pet:
    def __init__(self, nome, especie, idade, raca, peso, 
                 nome_dono, telefone_dono, vacinado, observacoes, hospedado=False):
        
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.nome_dono = nome_dono
        self.telefone_dono = telefone_dono
        self.observacoes = observacoes
        self.hospedado = hospedado
        
        # SOLUÇÃO PARA O ERRO 'lower': Detecta se o dado antigo era Booleano (True/False)
        if isinstance(vacinado, bool):
            self.vacinado = "sim" if vacinado else "não"
        else:
            self.vacinado = str(vacinado).lower().strip()
        
        # Encapsulamento do peso
        self._peso = float(peso)

    # Getter para o peso
    @property
    def peso(self):
        return self._peso

    # Setter para o peso (validação de segurança)
    @peso.setter
    def peso(self, novo_peso):
        if novo_peso > 0:
            self._peso = float(novo_peso)
        else:
            print("[Erro] O peso deve ser maior que zero.")

    def exibir_dados(self):
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Telefone: {self.telefone_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado == 'sim' else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        print(f"Observações: {self.observacoes}")

    def calcular_diaria(self):
        if self.idade <= 3:
            return 50.0
        elif self.idade <= 10:
            return 60.0
        else:
            return 75.0

    def registro_entrada(self):
        if self.hospedado:
            print(f"\n[Aviso] {self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"\n[Sucesso] {self.nome} entrou no hotel.")

    def registro_saida(self):
        if not self.hospedado:
            print(f"\n[Aviso] {self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"\n[Sucesso] {self.nome} saiu do hotel.")

    def verificar_vacinacao(self):
        if self.vacinado == 'sim':
            print(f'\n{self.nome}: Vacinado')
        else:
            print(f'\n{self.nome}: Não vacinado')

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso  # Dispara o setter para validar
        print(f'\n{self.nome}: Peso atualizado para {self.peso} kg')

    def emitir_resumo(self):
        valor = self.calcular_diaria()
        status_vacina = "Vacinado" if self.vacinado == 'sim' else "Não vacinado"
        return (
            f"\n===== RESUMO: {self.nome} ====="
            f"\nEspécie: {self.especie}"
            f"\nPeso: {self.peso} kg"
            f"\nDiária: R$ {valor:.2f}"
            f"\nStatus Vacina: {status_vacina}"
            f"\nHospedado: {'Sim' if self.hospedado else 'Não'}\n"
        )

    def para_dicionario(self):
        """Conversão necessária para salvar em JSON."""
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "raca": self.raca,
            "peso": self.peso,
            "nome_dono": self.nome_dono,
            "telefone_dono": self.telefone_dono,
            "vacinado": self.vacinado,
            "observacoes": self.observacoes,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """SOLUÇÃO PARA O ERRO 'KeyError': Usa .get() para chaves ausentes no JSON antigo."""
        return Pet(
            nome=dados.get("nome", "Sem nome"),
            especie=dados.get("especie", "Não informada"),
            idade=dados.get("idade", 0),
            raca=dados.get("raca", "SRD (Vira-lata)"),
            peso=dados.get("peso", 0.0),
            nome_dono=dados.get("nome_dono", "Não informado"),
            telefone_dono=dados.get("telefone_dono", "Não informado"),
            vacinado=dados.get("vacinado", "não"),
            observacoes=dados.get("observacoes", ""),
            hospedado=dados.get("hospedado", False)
        )


# =====================================================
# FUNÇÕES DE PERSISTÊNCIA (JSON)
# =====================================================

def salvar_pets(lista_pets):
    lista_dicionarios = [pet.para_dicionario() for pet in lista_pets]
    try:
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)
        print("\n[Sucesso] Dados salvos com sucesso em pets.json!")
    except IOError:
        print("\n[Erro] Falha ao salvar os dados no arquivo.")


def carregar_pets():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            lista_dicionarios = json.load(arquivo)
        return [Pet.criar_de_dicionario(dados) for dados in lista_dicionarios]
    except (json.JSONDecodeError, IOError):
        print("\n[Sistema] Erro ao ler arquivo. Iniciando banco de dados vazio.")
        return []


# =====================================================
# INTERFACE DO USUÁRIO E MENUS
# =====================================================

def cadastrar_pet(lista_pets):
    print("\n===== Cadastro de Pet =====")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0: raise ValueError
            break
        except ValueError:
            print("Digite uma idade inteira e positiva.")

    raca = input("Raça: ")
    
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso <= 0: raise ValueError
            break
        except ValueError:
            print("Digite um peso válido (maior que zero).")

    nome_dono = input("Nome do dono: ")
    telefone_dono = input("Telefone do dono: ")
    vacinado = input("Vacinado (sim/não): ")
    observacoes = input("Observações: ")

    novo_pet = Pet(nome, especie, idade, raca, peso, nome_dono, telefone_dono, vacinado, observacoes)
    lista_pets.append(novo_pet)
    print("\n[Sucesso] Pet cadastrado com sucesso!")


def listar_pets(lista_pets):
    if not lista_pets:
        print("\nNenhum pet cadastrado.")
        return False

    print(f"\n===== Lista de Pets ({len(lista_pets)}) =====")
    for i, pet in enumerate(lista_pets, 1):
        print(f"[{i}] {pet.nome} ({pet.especie}) - {'Hospedado' if pet.hospedado else 'Disponível'}")
    return True


def gerenciar_status_pet(lista_pets, acao):
    if not listar_pets(lista_pets):
        return

    try:
        numero = int(input(f"\nEscolha o número do pet para {acao}: "))
        idx = numero - 1

        if 0 <= idx < len(lista_pets):
            if acao == "Entrada":
                lista_pets[idx].registro_entrada()
            elif acao == "Saída":
                lista_pets[idx].registro_saida()
            elif acao == "Resumo":
                print(lista_pets[idx].emitir_resumo())
            elif acao == "Alterar Peso":
                novo_peso = float(input(f"Digite o novo peso de {lista_pets[idx].nome}: "))
                lista_pets[idx].atualizar_peso(novo_peso)
            elif acao == "Ficha Detalhada":
                lista_pets[idx].exibir_dados()
        else:
            print("\n[Erro] Número inválido.")
    except ValueError:
        print("\n[Erro] Entrada de dados inválida.")


def menu():
    pets = carregar_pets()

    while True:
        print("\n========== HOTEL PET SYSTEM ==========")
        print("1 - Cadastrar pet")
        print("2 - Listar nomes / Ficha detalhada")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Emitir resumo financeiro (Diária)")
        print("6 - Atualizar peso do pet")
        print("7 - Salvar dados manualmente")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_pet(pets)
        elif opcao == "2":
            gerenciar_status_pet(pets, "Ficha Detalhada")
        elif opcao == "3":
            gerenciar_status_pet(pets, "Entrada")
        elif opcao == "4":
            gerenciar_status_pet(pets, "Saída")
        elif opcao == "5":
            gerenciar_status_pet(pets, "Resumo")
        elif opcao == "6":
            gerenciar_status_pet(pets, "Alterar Peso")
        elif opcao == "7":
            salvar_pets(pets)
        elif opcao == "0":
            salvar_pets(pets)  # Auto-salvamento preventivo ao fechar
            print("\nSistema encerrado com segurança. Até logo!")
            break
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu()