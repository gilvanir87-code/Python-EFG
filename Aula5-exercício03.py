print("\n=======================================\n")

print("============= Cabeçalho Geral =============")

#usando as F-Strings e acessando as chaves


print("aluno",nome["Gilvanir"])
print("disciplina",disciplina["Python Básico"])
print("nota",nota["nota"])

print(f"👤Aluno(a): {aluno['nome']}")
print(f"📚Disciplina: {aluno['disciplina']}")
print(f"🗓Nota Final: {aluno['nota']}")

from datetime import datetime
data_formatada = datetime.now().strftime("%d/%m/%Y")
#Usando f-string para juntar o texto com a variável
print(f"🗓Data {data_formatada}")
#Saída: Data 16/16/2026

print("===========================================")
