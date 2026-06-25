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



print("============ Preço Inteligente ============")

produto = input("Nome do produto: ")
preco = float(input("Preço do produto: "))

if preco > 49.99:
    desconto = preco * 0.20
    preco_final = preco - desconto
    print(f"{produto} com desconto de 20% é: R$ {preco_final:.2f}")
elif preco >= 100:
    print(f"{produto} preço normal: R$ {preco:.2f}")
else:
    print(f"{produto} barato: R$ {preco:.2f}")
