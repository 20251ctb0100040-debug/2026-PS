# ===================================================
#SISTEMA DE CONVERSÃO DE UNIDADES
#====================================================
#Disciplina : Programação de Sistmas (PS)
# Aula      : 07 - Revisão: Módulos
# Autor     : [Luis Gustavo Pereira Melo]
#Data       : [05/03/2026]
# Repositorio:  https://github.com/20251ctb0100040-debug/2026-PS
#====================================================

# BLOCO 1: STDLIB

#----- BLOCO 2: MÓDULO PRÓPRIO -----
from conversores import temperatura #importa o módulo do pacote
print("\n==== Conversão de temperatura ===")
valor = 100.0
print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f}°F")
print(f"{valor}°C = {temperatura.celsius_para_kelvin(valor):.2f} K")
print(f"Zero absoluto: {temperatura.ZERO_ABSOLUTO_CELSIUS}°C")
k_valor = 373.15
print(f"{k_valor} K = {temperatura.kelvin_para_celsius(k_valor):.2f}")

#----bloco 3: API LIMPA DO PACOTE ----
from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes,
    kg_para_libras, kg_para_gramas
)

from utils import cabecalho_secao, formatar_resultado, linha_separadora


def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input("  Valor em °C: "))
    print(formatar_resultado("°C → °F", valor, "°C",
    celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C → K", valor, "°C", celsius_para_kelvin(valor),
    "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input("  Valor em km: "))

    print(formatar_resultado("km → mi", valor,
    "km", km_para_milhas(valor), "mi"))

    print(formatar_resultado("km → pés", valor * 1000, "m", metros_para_pes(valor
    * 1000), "pés"))

def menu_massa():
    print(cabecalho_secao("Conversão de Massa"))

    valor = float(input("  Valor em kg: "))

    print(formatar_resultado(
        "kg → lb", valor, "kg",
        kg_para_libras(valor), "lb"
    ))

    print(formatar_resultado(
        "kg → g", valor, "kg",
        kg_para_gramas(valor), "g"
    ))

def main():
    print(linha_separadora())
    print("  SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())

    opcoes = {
    "1": menu_temperatura,
    "2": menu_distancia,
    "3": menu_massa
}

    while True:
        print("\n  [1] Temperatura  [2] Distância  [3] Massa  [0] Sair")
        escolha = input("  Opção: ").strip()

        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    main()