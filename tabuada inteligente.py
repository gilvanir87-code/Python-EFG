# Gabarito: Desafio da tabuada (AULA 06)

print("========== Taqbua Inteligente ==========")
#Captura o número digitado pelo usuário (lembre-se do int!)
numero = int(input("Digite um número para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("== Multiplicação ==")

# O range(1, 11) vai gerar os números de 1 até 10
#(o último número no range sempre é ignorado)
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(numero, "X", multiplicador, "=", resultado)

print("== Adição ==")

for adicao in range(1, 11):
    resultado = numero + adicao
    print(numero, "+", adicao, "=", resultado)

print("== Subtração ==")

for subtracao in range(1, 11):
    resultado = numero - subtracao
    print(numero, "-", subtracao, "=", resultado)

print("== Divisão ==")

for divisor in range(1, 11):
    resultado = numero // divisor
    print(numero, "/", divisor, "=", resultado)

print("=================")
