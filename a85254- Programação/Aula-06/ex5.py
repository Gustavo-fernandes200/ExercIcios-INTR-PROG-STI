# Função para inicializar o tabuleiro
def criar_tabuleiro():
    return [[0 for i in range(7)] for i in range(6)]


# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))
    print()

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificar vitória na horizontal
    for linha in tabuleiro:
        for i in range(4):
            if all(cell == jogador for cell in linha[i:i+4]):
                return True

    # Verificar vitória na vertical
    for coluna in range(7):
        for i in range(3):
            if all(tabuleiro[i][coluna] == jogador for i in range(i, i+4)):
                return True

    # Verificar vitória na diagonal (ascendente)
    for i in range(3, 6):
        for j in range(4):
            if tabuleiro[i][j] == jogador and tabuleiro[i-1][j+1] == jogador and tabuleiro[i-2][j+2] == jogador and tabuleiro[i-3][j+3] == jogador:
                return True

    # Verificar vitória na diagonal (descendente)
    for i in range(3):
        for j in range(4):
            if tabuleiro[i][j] == jogador and tabuleiro[i+1][j+1] == jogador and tabuleiro[i+2][j+2] == jogador and tabuleiro[i+3][j+3] == jogador:
                return True

    return False

# Função principal para o jogo
def jogo_quatro_em_linha():

    tabuleiro = criar_tabuleiro()
    jogador = 1
    imprimir_tabuleiro(tabuleiro)

    while True:
        while True:
            coluna = int(input(f"Jogador {jogador}, escolha uma coluna (0-6): "))

            # Verificar se a coluna está cheia ou inválida
            if coluna < 0 or coluna > 6:
                print("Escolha uma coluna válida (0-6).")
            elif 0 not in [linha[coluna] for linha in tabuleiro]:
                print("Essa coluna está cheia. Escolha outra.")
            else:
                # Colocar a peça na coluna escolhida
                for i in range(5, -1, -1):
                    if tabuleiro[i][coluna] == 0:
                        tabuleiro[i][coluna] = jogador
                        break
                break
        imprimir_tabuleiro(tabuleiro)

        # Verificar se o jogador venceu
        if verificar_vitoria(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            break

        # Alternar jogadores
        jogador = 3 - jogador


if __name__ == "__main__":
    jogo_quatro_em_linha()

