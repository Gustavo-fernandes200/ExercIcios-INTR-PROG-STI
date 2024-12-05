from random import randint
import random


def main():
    jogoDaGloria()


def jogoDaGloria():

    jogador1_posicao = 0
    jogador2_posicao = 0

    permissao_jogador1 = True
    permissao_jogador2 = True

    tabuleiro = list(range(0, 51))

    print("Boas!! Seja Bem-vindo ao jogo da gloria : ")

    jogador1_nome = input("Por favor, introduza o seu nome para dá inicio ao jogo da gloria. Obrigado :) : ")
    jogador2_nome = input("Por favor, introduza o seu nome para dá inicio ao jogo da gloria. Obrigado :) : ")

    print(
        f"{jogador1_nome} e o {jogador2_nome}, Este é o inicio do jogo. Cada um de vocês, "
        f"tem o direito de lancarem dois dados de 6 lados : ")

    while True:


        mostrar_tabuleiro(tabuleiro, jogador1_posicao, jogador2_posicao)

        if permissao_jogador1:

            # Jogador 1 faz seus lançamentos
            jogador1_posicao += lancamentos_de_dados_dos_jogadores(jogador1_nome)

            jogador1_posicao, permissao_jogador1 = processar_condiçoes_e_posicoes_dos_jogadores(jogador1_nome,jogador1_posicao)

            # realizacao_avancar_casas(jogador1_nome, soma_jogador1, lancou_jogador1, jogador1_posicao)

        else:
            permissao_jogador1 = True

        if permissao_jogador2:

            # Jogador 1 faz seus lançamentos
            jogador2_posicao += lancamentos_de_dados_dos_jogadores(jogador2_nome)

            jogador2_posicao, permissao_jogador2 = processar_condiçoes_e_posicoes_dos_jogadores(jogador2_nome,jogador2_posicao)

            # realizacao_avancar_casas(jogador2_nome, soma_jogador2, lancou_jogador2, jogador2_posicao)

        else:
            permissao_jogador2 = True


def lancamentos_de_dados_dos_jogadores(jogador_nome):

        input(
            f"Olá {jogador_nome}, para quiser fazer os lançamentos dos dois dados é preciso que você clique a tela Enter. "
            f"Obrigado!! : ")

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        soma = dado1 + dado2

        print(f"{jogador_nome}, a soma dos dados foi {soma}")

        return soma


def realizacao_avancar_casas(jogador_nome, soma_dados, lancou_jogador, posicao_atual):

        if lancou_jogador:

            for i in range(1, 51):

                if soma_dados == i:
                    print(f"{jogador_nome} acertou {i}! Avance para a casa {i}.")
                    posicao_atual = i
                    return i

        return realizacao_avancar_casas("Jogador1" "jogador2", "{i}", True , "{i]")


def mostrar_tabuleiro(tabuleiro, jogador1, jogador2):

        tabuleiro_interno = tabuleiro.copy()

        tabuleiro_interno[jogador1] = " Jogador1"

        if type(tabuleiro_interno[jogador2]) == int:
            tabuleiro_interno[jogador2] = " Jogador2"
        else:
            tabuleiro_interno[jogador2] += " Jogador2"

        previous_i = 0
        inverter_tabuleiro = False

        for i in range(10, len(tabuleiro), 10):

            if not inverter_tabuleiro:

                for j in tabuleiro_interno[previous_i:i]:
                    print(f"{j}", end="  ")
                print()
                inverter_tabuleiro = True

            else:

                for k in list(reversed(tabuleiro_interno[previous_i:i])):
                    print(f"{k}", end="  ")
                print()
                inverter_tabuleiro = False

            previous_i = i


def processar_condiçoes_e_posicoes_dos_jogadores(jogador_nome, posicao_atual):

        if posicao_atual == 3 or posicao_atual == 8:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você conseguiu avançar três casas, "
                  f"após do seu lançamentos em diante. Grande sorte que você calhou ")

            return posicao_atual + 3, True

        elif posicao_atual == 5:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você parenceu na mesma casa "
                  f"Grande Azar que você calhou ")

            return 0, True

        elif posicao_atual == 16 or posicao_atual == 35:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Não joga na próxima rodada."
                  f"Grande Azar que você calhou ")

            return posicao_atual, False

        elif posicao_atual == 22:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você conseguiu avançar duas casas, "
                  f"após do seu lançamentos em diante. Grande sorte que você calhou ")

            return posicao_atual + 2, True

        elif posicao_atual == 31:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você conseguiu avançar duas casas, "
                  f"após do seu lançamentos em diante. Grande sorte que você calhou ")

            return posicao_atual + 1, True

        elif posicao_atual == 31:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você conseguiu avançar uma casas, "
                  f"após do seu lançamentos em diante. Que sorte você calhou ")

            return posicao_atual + 1, True

        elif posicao_atual == 38:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você conseguiu avançar quatro casas, "
                  f"após do seu lançamentos em diante. Grande sorte você calhou ")

            return posicao_atual + 4, True

        elif posicao_atual == 44 or posicao_atual == 49:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você recuou quatro casas, "
                  f"após do seu lançamentos em diante. Grande azar que você calhou ")

            return posicao_atual - 4, True

        else:
            return posicao_atual, True

"""
        if posicao_atual == 27:

            print(f"{jogador_nome}, você está na casa {posicao_atual}. Você calhou ter a casa partilha com outro jogador, "
                  f"após do seu lançamentos em diante. Grande azar você calhou ")

            return jogador_nome
        return False
"""


if __name__ == "__main__":
    jogoDaGloria()
