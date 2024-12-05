# Solicita os lados da figura ao usuário
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))

# Calcula a área da figura
area = lado1 * lado2

# Verifica se é um quadrado ou retângulo
if lado1 == lado2:
    print(f"A área da figura é: {area}")
    print("É um quadrado.")
else:
    print(f"A área da figura é: {area}")
    print("É um retângulo.")
