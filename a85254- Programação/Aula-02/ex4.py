import math

# Solicita o raio da circunferência ao usuário
raio = float(input("Digite o raio da circunferência: "))

# Calcula o perímetro da circunferência
perimetro = 2 * math.pi * raio

# Calcula a área da circunferência
area = math.pi * raio ** 2

# Exibe o perímetro e a área da circunferência
print(f"O perímetro da circunferência é: {perimetro:.2f}")
print(f"A área da circunferência é: {area:.2f}")
