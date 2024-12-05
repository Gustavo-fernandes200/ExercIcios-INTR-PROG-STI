
# Solicita ao usuário para inserir o número para o qual a tabuada será calculada
numero = int(input("Digite um número para a tabuada: "))

# Calcula e imprime a tabuada do número fornecido
print("Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
