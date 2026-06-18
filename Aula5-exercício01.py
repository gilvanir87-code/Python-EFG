#Nome: Gilvanir dos Santos e Sousa
#Data: 16/06/2026
#Professor: Rodrigo Vilela
#Python Básico

#1. Criando um dicionário com dados de alunos

print("\n=========== Sistema Escolar ===========\n")

aluno = {
    "nome":input("Digite o nome do aluno: "),
    "disciplina":"Python Básico",
    "nota":float(input("Digite a nota final (ex: 8.5): "))
}
print("\n======== Analisando resultado =========\n")
print("Aluno", aluno["nome"])
print("Nota", aluno["nota"])

#2. Usando IF e ELSE para tomar uma decisão
# Se(IF) a nota for maior ou igual a 6.0, ele está aprovado. SENÃO (ELSE), reprovado
if aluno["nota"]>=6.0:
    print("O aluno está APROVADO! Parabéns");
else:
        print("REPROVADO! Estude mais!!")


print("\n=======================================")
