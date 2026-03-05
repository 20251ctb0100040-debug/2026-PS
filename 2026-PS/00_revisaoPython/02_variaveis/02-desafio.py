# Programação de sistema.
# Luis Gustavo Pereira Melo 
# Repositorio:https://github.com
# Descrição: criar um programa que adicione novos itens ao estoque da loja avaliando se quantidade for 5 é critico, de 5 a 20 adequado e mais e 20 exelente.

# Minha lista inicial com os dados base da loja
estoque = [
    {"nome": "CPU", "Quantidade": 4},
    {"nome": "placa-mãe", "Quantidade": 10},
    {"nome": "memoria ram", "Quantidade": 7},
    {"nome": "SSD/HD", "Quantidade": 20},
    {"nome": "Mouse", "Quantidade": 15},
    {"nome": "Teclado", "Quantidade": 1}
]

# Cadastro de novos produtos com trava de segurança (não aceita letras ou números negativos)
for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    while True:
        try:
            quant = int(input(f"Indique a quantidade de {nome}: "))
            if quant < 0:
                print("Valor negativo não vale! Digite de novo.")
                continue
            break
        except ValueError:
            print("Isso não é um número! Digite a quantidade em algarismos.")
    
    estoque.append({"nome": nome, "Quantidade": quant})

print("\n============ ESTOQUE ATUALIZADO ============")

# Criei essas variáveis para fazer o resumo final que o gerente pediu
criticos = 0
adequados = 0
excelentes = 0
mais_critico = estoque[0] # Começo achando que o primeiro é o menor para comparar

for item in estoque:
    quant = item["Quantidade"]
    
    # Aqui o sistema decide a situação baseada nos valores que o gerente passou
    if quant < 5:
        situacao = "CRÍTICA ‼️"
        criticos += 1
    elif 5 <= quant <= 20:
        situacao = "ADEQUADO 😐"
        adequados += 1
    else:
        situacao = "EXCELENTE ✨"
        excelentes += 1
    
    # Lógica para descobrir qual produto está com a menor quantidade de todos
    if quant < mais_critico["Quantidade"]:
        mais_critico = item
    
    # Mostra a linha do produto arrumadinha com o sinalizador
    print(f"Produto: {item['nome']:<15} | Quantidade: {quant:<5} | Situação: {situacao}")

# Exibe o resumo de contagem e o alerta do item mais escasso
print("-" * 50)
print(f"RESUMO: {criticos} Críticos | {adequados} Adequados | {excelentes} Excelentes")
print(f"🚨 ATENÇÃO: O item mais crítico é {mais_critico['nome']} com apenas {mais_critico['Quantidade']} unidades.")
print("=" * 50)

# Sistema de busca para o gerente não precisar ler a lista toda toda vez
while True:
    busca = input("\nQuer pesquisar um produto específico? (ou digite 'sair'): ").strip().lower()
    if busca == 'sair':
        break
    
    achou = False
    for item in estoque:
        if item["nome"].lower() == busca:
            print(f"✅ Resultado: {item['nome']} tem {item['Quantidade']} no estoque.")
            achou = True
            break
    
    if not achou:
        print("❌ Esse produto não consta no nosso sistema.")

print("\nPrograma finalizado com sucesso!")
