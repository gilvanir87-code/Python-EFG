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

print("===========================================")
