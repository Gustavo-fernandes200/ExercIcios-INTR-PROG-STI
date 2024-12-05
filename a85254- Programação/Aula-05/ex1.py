# Função para calcular a potência de um número
def calcular_potencia(base, expoente):
    resultado = 1
    for i in range(expoente):
        resultado *= base
    return resultado

# Entrada de dados
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Chamando a função para calcular a potência
resultado_potencia = calcular_potencia(base, expoente)

# Exibindo o resultado
print(f"{base} elevado a {expoente} é igual a {resultado_potencia}")
