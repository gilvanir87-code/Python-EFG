#Nome: Gilvanir dos Santos e Sousa
#Data: 12/06/2026
#Professor: Rodrigo Vilela
#Python Básico

print("\n================== Exercício 01 - Aula 4 ==================\n")
# Criar uma lista de Strings chamada FRUTAS com 5 elementos

frutas = ["maçã", "goiaba", "manga", "uva", "tangerina"]

print(frutas)

# Conta a quantidade de elementosna lista "frutas" e guarda a variável
# "total_frutas"

total_frutas = len(frutas)

# Exibe na tela o valor da variável "total_frutas" (que é 5)
print("\nTotal de frutas na nossa lista é: ", total_frutas)


print("\n================== LISTA DE ALUNOS ==================\n")
# Cria uma nova lista chamada "alunos" com 5 nomes
alunos = ["José", "Amanda", "Jubileu", "Tônho", "Alfredina"]

print(alunos)

# Exibe o primeiro elemento da lista "alunos" (índice 0 é "José")
print("\nAluno 1: ",alunos[0])
print("Aluno 2: ",alunos[1])
print("Aluno 3: ",alunos[2])
print("Aluno 4: ",alunos[3])
print("Aluno 5: ",alunos[4])

print(f"{alunos[0]}\n{alunos[3]}")

print("\n========== APPEND para inserir no final da lista ==========\n")

# INSERÇÃO: Adcionar o nome "Pedro" no final da lista
print("O aluno Pedro entrou na lista na posição final da lista\n")
alunos.append("Pedro")
print(alunos)

# MUDAR a posição de Pedro
alunos.insert(1, "Pedro")
print(alunos)


# EXCLUSÂO: remover um aluno da lista procurando pelo nome
alunos.remove("Pedro") #pode colocar o nome do aluno dentro de aspas ""
alunos.remove("Pedro")
print(alunos)
print("\n===========================================================\n")
