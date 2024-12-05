# Solicita a quantidade de euros a serem convertidos
euros = float(input("Digite a quantidade de euros que deseja converter: "))

# Taxa de conversão de euros para dólares
taxa_conversao = 1.17

# Calcula a quantidade equivalente em dólares
dolares = euros * taxa_conversao

# Exibe o resultado da conversão
print(f"{euros} euros equivalem a {dolares} dólares.")
