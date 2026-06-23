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

print("===========================================\n")

import random
print("========== Aula 8 - Exercício 01 ==========")
print("\n========= Sistema de Loja Virtual =========\n")

#=========================================
#Função 1. Exibe a mensagem de boas vindas
#=========================================

def exibir_mensagem():
    print("Bem vindo(a) à nossa loja!")
    print("Hoje você poderá ganhar um cupom de desconto em nossa loja, APROVEITE!")

#Função 2. calcula o desconto
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual/100)
    preco_final = preco - desconto
    return preco_final

#Recebendo informações do usuário
nome_produto = input("\nDigite o nome do produto: ")

valor_produto = float(
    input("Digite o valor do produto: R$ ")
)
#Sorteando um cupom de desconto
desconto_sorteado = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 99])

print(f"\n PARABÉNS! Você ganhou {desconto_sorteado}% de desconto!")

#==========================
#Chamando a função calcular
#==========================
valor_final = calcular_desconto(
    valor_produto,
    desconto_sorteado
)

#Exibindo o resultado
print("\n==== Resumo da Compra ====")
print(f"=>Produto: {nome_produto}")
print(f"=>Valor original: R$ {valor_produto:.2f}")
print(f"=>Desconto: {desconto_sorteado}%")
print(f"=>Valor Final: R$ {valor_final:.2f}")
print("="*26)

