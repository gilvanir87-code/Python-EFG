#Nome: Gilvanir dos Santos e Sousa
#Data: 11/06/2026
#Professor: Rodrigo Vilela
#Python Básico

print("\n==================== Exercício 02 - Aula 3 ====================\n")
print("\n======== Gerando o crachá =========\n")

# 1. Receba o nome do usuário
nome_bruto = input("Digite seu nome completo: ")

# 2. Substitua os traços por espaços
nome_sem_tracos = nome_bruto.replace("-" , " ")

# 3. Converta tudo para maiúsculo
nome_cracha = nome_sem_tracos.upper()

# 4. Descubra o tamanho do nome
tamanho = len(nome_cracha)

# 5. Imprima o resultado final

print("CRACHÁ Gerado:  " + nome_cracha)
print("Caracteres utilizados: ", tamanho)


print("\n================================================================\n")
