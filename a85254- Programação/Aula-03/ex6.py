#Implemente um programa para calcular o fatorial de um número

# Entrada do Usuário:
num = int(input("Digite um número para calcular o fatorial: "))

# Definição da Função fatorial:
def fatorial(num):

    # Verificação de Números Negativos:
    if num < 0:
        print("O fatorial não está definido para números negativos.")
        return None

    # Cálculo do Fatorial:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    # Retorno do Resultado:
    return factorial

# Chamada da Função e Impressão do Resultado:
resultado = fatorial(num)
if resultado is not None:
    print(f"O fatorial de {num} é {resultado}.")
