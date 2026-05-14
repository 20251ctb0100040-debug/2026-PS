'''
=====================================================
# ARQUIVO : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula : Aula 20 - Por que POO?
# Autor: Luis Gustavo Pereira
# Conceitos :Classe, objeto, atributos, métodos, encapsulamento
#Atividade : Classe Pet
=====================================================
'''




class Pet:
    '''
    Esta classe representa um pet em um sistema simpes de hotel para 
    pets.
    
    Em vez de guardar os dados do pet em um dicionario solto, como
    faziamos
    na programação estruturada, agora agrupamos os dados e comportamentos
    dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, raca, peso, nome_dono, telefone_dono, vacinado, observacoes):
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
        print(f" Nome do dono: {self.nome_dono}")
        print(f"Telefone: {self.telefone_dono}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registro_entrada(self):
        if self.hospedado:
            print(f"Aviso: {self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")

    def registro_saida(self):
        if not self.hospedado:
            print(f"Aviso: {self.nome} não está hospedado")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")
    
    def verificar_vacinacao(self):
        if self.vacinado == 'sim':
            print(f'{self.nome} Vacinado')
        else:
            print(f'{self.nome} Não vacinado')

    def calcular_diaria(self):
        if self.idade <= 3:
            return 50
        elif self.idade <= 10:
            return 60
        else:
            return 75  
        
    def atualizar_peso(self, novo_peso):
        self.peso = float(novo_peso)
        print(f'{self.nome} Peso atualizado para {self.peso} kg')

    def emitir_resumo(self):
        valor_diaria = self.calcular_diaria()
        return (
            f"Nome: {self.nome}\n"
            f"Vacinação: {'Sim' if self.vacinado == 'sim' else 'Não'}\n"
            f"Hospedagem: {'Sim' if self.hospedado else 'Não'}\n"
            f"Valor: R$ {valor_diaria:.2f}"
        )



pet1 = Pet("Rex", "Cachorro", 5, "Labrador", 22.5, "Maria", "42999999999", "sim", "Nenhuma")
pet2 = Pet("Mimi", "Gato", 2, "Siamês", 4.2, "João", "41988888888", "sim", "Alergia leve")
pet3 = Pet("Thor", "Cachorro", 11, "Vira-lata", 18.0, "Ana", "41977777777", "não", "Idoso")

pet1.exibir_dados()
pet1.registro_entrada()
pet1.verificar_vacinacao()
pet1.atualizar_peso(23.0)
pet1.emitir_resumo()
pet2.exibir_dados()
pet2.registro_entrada()
pet2.verificar_vacinacao()
pet2.emitir_resumo()
pet3.exibir_dados()
pet3.registro_entrada()
pet3.verificar_vacinacao()
pet3.emitir_resumo()
