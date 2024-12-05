numero = int(input("Digite um número inteiro: "))

# Inicializa menor_algorismo com o primeiro dígito do número
menor_algorismo = numero % 10

# Remove o último dígito do número inicial
numero //= 10

while numero > 0:
    digito = numero % 10
    if digito < menor_algorismo:
        menor_algorismo = digito
    numero //= 10

print(f"O menor algarismo no número digitado é: {menor_algorismo}")

# Exemplo de vetor (lista)
vetor = [5, 2, 9, 1, 7, 3, 8, 10]

# Inicializa contadores para valores pares e ímpares
num_pares = 0
num_impares = 0

# Itera sobre o vetor para contar pares e ímpares
for num in vetor:
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

# Imprime o número de valores pares e ímpares
print("Número de valores pares:", num_pares)
print("Número de valores ímpares:", num_impares)
