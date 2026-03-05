# Arquivo: 0lb-debug.py
# ATENÇÃO: Este código contém 4 erros propositais. Encontre e corrija todos!
nome = input("Digite o nome do aluno: ") #input errado tava imput
nota1 = float (input("Digite a nota 1: ")) 
nota2 = float (input("Digite a nota 2: "))
media = (nota1 + nota2) / 2 # erro logico
if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else: #identação tava errada
    situacao ="Reprovado"
    
print (f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")#erro no print (tava pront)