#Nome: Gilvanir dos Santos e Sousa
#Data: 11/06/2026
#Professor: Rodrigo Vilela
#Python Básico

#---live code: Aula 3 - Tipos de Dados e Strings

#trabalhando com números (int e float)
print("\n==================== Exercício 01 - Aula 3 ====================\n")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (Ex: 1.75): "))

#2. Manipulação de textos (Strings)
frase = input("Digite uma frase que você gosta: ")

print("\n==================== ANALISANDO SEUS DADOS ====================\n")

# Fazendo cálculos simples com os números
print("Sua idade daqui 5 anos será: ", idade+5)
print("Sua altura em centímetros é: ", altura*100, "cm")

# Usando Métodos de Strings
# Explicando o .upper(), .lower() e o len() fazem

print("Sua frase toda em MAIÚSCULAS: ", frase.upper())
print("Sua frase toda em minúscula: ", frase.lower())
print("A frase digitada tem: ", len(frase), "caracteres (incluindo espaços)")

print("\n================================================================\n")
