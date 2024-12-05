# Inicializa um vetor para armazenar os valores lidos
def ler_valores():
    valores = []
    for i in range(10):
        while True:
            valor_entrada = input("Introduza um valor inteiro: ")
            if valor_entrada.isdigit():
                valor = int(valor_entrada)
                valores.append(valor)
                break
            else:
                print("Por favor, introduza um valor inteiro válido.")
    return valores

def calcular_diferenca(valores):
    maior_valor = max(valores)  # Encontra o maior valor no vetor
    menor_valor = min(valores)  # Encontra o menor valor no vetor
    diferenca = maior_valor - menor_valor  # Calcula a diferença
    return diferenca

def contagem_num_impares_pares(valores):
    num_pares = 0
    num_impares = 0
    for num in valores:
        if num % 2 == 0:
            num_pares += 1
        else:
            num_impares += 1
    return num_pares,num_pares


valores = ler_valores()
print("Os valores lidos são:", valores)

diferenca = calcular_diferenca(valores)
print("Diferença entre o maior e o menor valor:", diferenca)

num_pares, num_impares = contagem_num_impares_pares(valores)
print("Número de valores pares:", num_pares)
print("Número de valores ímpares:", num_impares)
