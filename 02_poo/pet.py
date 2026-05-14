'''
=====================================================
# ARQUIVO : pet.py
# Disciplina : Programação de Sistemas (2026-2)
# Aula : Aula 20 - Por que POO?
# Autor: Luis Gustavo Pere]
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

    def calcular_diaria(self):
        if self.idade <= 3:
            return 50
        elif self.idade <= 10:
            return 60
        else:
            return 75

    def emitir_resumo(self):
        valor_diaria = self.calcular_diaria()
        return (
            f"Nome: {self.nome}\n"
            f"Vacinação: {'Sim' if self.vacinado == 'sim' else 'Não'}\n"
            f"Hospedagem: {'Sim' if self.hospedado else 'Não'}\n"
            f"Valor: R$ {valor_diaria:.2f}"
        )


# Criando corretamente os objetos
pet1 = Pet("Rex", "Cachorro", 5, "Labrador", 22.5, "Maria", "42999999999", "sim", "Nenhuma")
pet2 = Pet("Mimi", "Gato", 2, "Siamês", 4.2, "João", "41988888888", "sim", "Alergia leve")
pet3 = Pet("Thor", "Cachorro", 11, "Vira-lata", 18.0, "Ana", "41977777777", "não", "Idoso")

# Chamadas corretas
pet1.registro_entrada()
print(pet1.emitir_resumo())