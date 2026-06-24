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

import random

def jogar_dado():
    return random.randint(1, 6)
print("\n======================= JOGANDO DADO =======================")
while True:
    opcao = input("\nDigite 'jogar' para lançar o dado ou 'sair' para encerrar: ").lower()

    if opcao == "sair":
        print("\nVocê saiu. Até Breve!")
        break
    elif opcao == "jogar":
        resultado = jogar_dado()
        print(f"\n🎲Saiu o número: {resultado}")
    else:
        print("\nOpção inválida. Jogue novamente.")

print("="*63)
