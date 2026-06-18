from datetime import datetime

# Dicionário com os dados do aluno
aluno = {
    "nome": "Gilvanir dos Santos",
    "disciplina": "Python Básico",
}

print("\n=======================================\n")
print("============= Cabeçalho Geral =============")

# Acessando os valores do dicionário
print("aluno:", aluno["nome"])
print("disciplina:", aluno["disciplina"])

# Usando f-strings
print(f"👤 Aluno(a): {aluno['nome']}")
print(f"📚 Disciplina: {aluno['disciplina']}")


# Data atual formatada
data_formatada = datetime.now().strftime("%d/%m/%Y")
print(f"🗓 Data: {data_formatada}")

print("=============================================================")

# Exercício 1. Usando FOR com range()
print("\n=========== Contagem Regressiva (FOR) ===========")
# O ranger(5, 0, -1) conta de 5 até 1, diminuindo 1 por vez

for numero in range(5, 0, -1):
    print("Faltam", numero, "segundos")
    print("⚡\n")

# Exemplo 2. Usando o WHILE com o comando BREAK
print("\n=========== Sistema de Senha (WHILE) ===========")

while True:
    senha = input("Digite uma senha secreta (ou SAIR para fechar): ")
    if senha == "000000":
        print("Acesso peritido! Bem-vindo")
        break # O break interrompe e destroi o loop imediatamente
    elif senha == "sair":
        print("Encerrando o programa")
        break
    else:
        print("Senha incorreta, tente novamente.\n")

print("\n===========================================================")
