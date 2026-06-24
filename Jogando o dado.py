import random

def rolar_dado():
    return random.randint(1, 6)
print("\n===================== Lançando o Dado =====================")
while True:
    opcao = input("\nDigite 'jogar' para lançar o dado ou 'sair' para encerrar: ").lower()

    if opcao == "sair":
        print("\nVocê saiu.")
        break
    elif opcao == "jogar":
        resultado = rolar_dado()
        print(f"\nSaiu o número: {resultado}")
    else:
        print("\nOpção inválida. Jogue novamente.")

print("="*59)
