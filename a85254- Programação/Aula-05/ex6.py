def procurar_numero(vetor, numero):
    if numero in vetor:
        return True
    else:
        return False


def main():
    vetor = [4, 1, 8, 3, 6, 2, 9, 5, 7]

    numero_procurado = 6

    encontrado = procurar_numero(vetor, numero_procurado)

    if encontrado:
        print(f"O número {numero_procurado} foi encontrado no vetor.")
    else:
        print(f"O número {numero_procurado} não foi encontrado no vetor.")


main()
