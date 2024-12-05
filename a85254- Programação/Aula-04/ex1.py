valores = []

# Leitura de 10 valores inteiros
for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    valores.append(valor)

# Encontrar o maior e o menor valor na lista
maior_valor = max(valores)
menor_valor = min(valores)

# Calcular a diferença entre o maior e o menor valor
diferenca = maior_valor - menor_valor

# Contagem de valores pares e ímpares
num_pares = sum(valor % 2 == 0 for valor in valores)
num_impares = len(valores) - num_pares

# Imprimir os resultados
print(f"Diferença entre o maior e o menor valor: {diferenca}")
print(f"Número de valores pares: {num_pares}")
print(f"Número de valores ímpares: {num_impares}")