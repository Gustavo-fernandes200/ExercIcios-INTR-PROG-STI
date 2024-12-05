
def maior_algarismo(numero):
    # Converte o número para uma lista de dígitos
    digitos = list(str(numero))

    # Encontra o maior dígito na lista e converte de volta para inteiro
    maior = int(max(digitos))

    return maior

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
resultado = maior_algarismo(numero)
print("O maior algarismo no número é:", resultado)

