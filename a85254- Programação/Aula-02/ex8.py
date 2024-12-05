# Solicita os três valores ao usuário
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# Inicializa uma variável para armazenar o máximo
maximo = valor1

# Compara os valores para encontrar o máximo
if valor2 > maximo:
    maximo = valor2
if valor3 > maximo:
    maximo = valor3

# Exibe o valor máximo
print(f"O valor máximo é: {maximo}")
