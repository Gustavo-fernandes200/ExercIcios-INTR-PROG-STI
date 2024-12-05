# jogos.py

def ex4():

    from time import sleep
    from random import randint
    import sys

    pts_jogador = 0
    pts_pc = 0
    nome_jogador = input("Digite seu nome para começar o jogo: ")

    while True:
        j = ''
        primeiro = ''
        p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
        lv = 'livre'
        pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
        jogada = 0
        jog_adv = 0
        jogada_aleatoria = 0
        turnos = 1
        vencedor = ''
        tabuleiro_inicial = '''
    --- COMO JOGAR ---

    "Quando for a sua vez, digite o número correspondente à posição no tabuleiro para fazer a sua jogada nela.

         |     |     
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     
        '''

        print(tabuleiro_inicial)

        while j != 'O' and j != 'X':
            j = str(input('Digite X ou O e em seguida pressione Enter: ')).strip().upper()
            if j != 'O' and j != 'X':
                print('\n Opção inválida!\n')

        if j == 'O':
            adv = 'X'
            print('\nEntão irei ficar com o X.')
        elif j == 'X':
            adv = 'O'
            print('\nEntão irei ficar com a O.')

        print('\nQuem joga primeiro?', end=' ')

        while primeiro != 'EU' and primeiro != 'PC':
            instr = 'Digite EU e pressione Enter para você começar, ou digite PC e pressione Enter para eu começar: '
            primeiro = str(input(instr)).strip().upper()
            if primeiro != 'EU' and primeiro != 'PC':
                print('\nEscolha inválida!\n')

        if primeiro == 'EU':
            print('\nEntão você joga primeiro.\n')
        elif primeiro == 'PC':
            print('\nEntão eu jogo primeiro.\n')

        def atualizar_tabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
            tabuleiro = '''
         |     |   
      {}  |  {}  |  {}
    _____|_____|_____
         |     |
      {}  |  {}  |  {}
    _____|_____|_____
         |     |
      {}  |  {}  |  {}
         |     |
            '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
            print(tabuleiro)

        def jogada_j1():
            jogada = 0

            while True:
                jogada = input('Digite a posição da sua jogada (1 a 9) e pressione Enter: ')
                if jogada.isdigit():
                    jogada = int(jogada)
                    if 1 <= jogada <= 9:
                        break
                    else:
                        print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')
                else:
                    print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')

        def rotina_j1():

            global jogada
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            msg_ocupado = '\nEste espaço já está ocupado!\n'

            jogada_j1()

            while jogada not in range(1, (9 + 1)):
                jogada_j1()

                if jogada not in range(1, (9 + 1)):
                    print('\nNúmero inválido!\n')

            while jogada == 1 and pos1 == 'ocupada' or \
                    jogada == 2 and pos2 == 'ocupada' or \
                    jogada == 3 and pos3 == 'ocupada' or \
                    jogada == 4 and pos4 == 'ocupada' or \
                    jogada == 5 and pos5 == 'ocupada' or \
                    jogada == 6 and pos6 == 'ocupada' or \
                    jogada == 7 and pos7 == 'ocupada' or \
                    jogada == 8 and pos8 == 'ocupada' or \
                    jogada == 9 and pos9 == 'ocupada':
                print(msg_ocupado)
                rotina_j1()

        def atualizar_jogadas_j1():

            global jogada
            global p1, p2, p3, p4, p5, p6, p7, p8, p9
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            if jogada == 1:
                p1 = j
                pos1 = 'ocupada'

            elif jogada == 2:
                p2 = j
                pos2 = 'ocupada'

            elif jogada == 3:
                p3 = j
                pos3 = 'ocupada'

            elif jogada == 4:
                p4 = j
                pos4 = 'ocupada'

            elif jogada == 5:
                p5 = j
                pos5 = 'ocupada'

            elif jogada == 6:
                p6 = j
                pos6 = 'ocupada'

            elif jogada == 7:
                p7 = j
                pos7 = 'ocupada'

            elif jogada == 8:
                p8 = j
                pos8 = 'ocupada'

            elif jogada == 9:
                p9 = j
                pos9 = 'ocupada'

        def atualizar_jogadas_j2():

            global jogada, jogada_aleatoria, adv
            global p1, p2, p3, p4, p5, p6, p7, p8, p9
            global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

            print('Deixe-me pensar na minha jogada...')
            sleep(1.5)
            jogada_aleatoria = randint(1, 9)

            while jogada_aleatoria == 1 and pos1 == 'ocupada' or \
                    jogada_aleatoria == 2 and pos2 == 'ocupada' or \
                    jogada_aleatoria == 3 and pos3 == 'ocupada' or \
                    jogada_aleatoria == 4 and pos4 == 'ocupada' or \
                    jogada_aleatoria == 5 and pos5 == 'ocupada' or \
                    jogada_aleatoria == 6 and pos6 == 'ocupada' or \
                    jogada_aleatoria == 7 and pos7 == 'ocupada' or \
                    jogada_aleatoria == 8 and pos8 == 'ocupada' or \
                    jogada_aleatoria == 9 and pos9 == 'ocupada':
                jogada_aleatoria = randint(1, 9)

            print('\nEu jogo na posição {}!'.format(jogada_aleatoria))

            if jogada_aleatoria == 1:
                p1 = adv
                pos1 = 'ocupada'
            elif jogada_aleatoria == 2:
                p2 = adv
                pos2 = 'ocupada'
            elif jogada_aleatoria == 3:
                p3 = adv
                pos3 = 'ocupada'
            elif jogada_aleatoria == 4:
                p4 = adv
                pos4 = 'ocupada'
            elif jogada_aleatoria == 5:
                p5 = adv
                pos5 = 'ocupada'
            elif jogada_aleatoria == 6:
                p6 = adv
                pos6 = 'ocupada'
            elif jogada_aleatoria == 7:
                p7 = adv
                pos7 = 'ocupada'
            elif jogada_aleatoria == 8:
                p8 = adv
                pos8 = 'ocupada'
            elif jogada_aleatoria == 9:
                p9 = adv
                pos9 = 'ocupada'

        def checar_vencedor():
            global j, adv, turnos, vencedor, pts_jogador, pts_pc
            global p1, p2, p3, p4, p5, p6, p7, p8, p9

            if p1 == j and p2 == j and p3 == j or \
                    p1 == j and p4 == j and p7 == j or \
                    p1 == j and p5 == j and p9 == j or \
                    p2 == j and p5 == j and p8 == j or \
                    p3 == j and p5 == j and p7 == j or \
                    p3 == j and p6 == j and p9 == j or \
                    p4 == j and p5 == j and p6 == j or \
                    p7 == j and p8 == j and p9 == j:
                print('VOCÊ GANHOU!\n')
                pts_jogador += 1
                vencedor = 'EU'
                turnos = 10

            if p1 == adv and p2 == adv and p3 == adv or \
                    p1 == adv and p4 == adv and p7 == adv or \
                    p1 == adv and p5 == adv and p9 == adv or \
                    p2 == adv and p5 == adv and p8 == adv or \
                    p3 == adv and p5 == adv and p7 == adv or \
                    p3 == adv and p6 == adv and p9 == adv or \
                    p4 == adv and p5 == adv and p6 == adv or \
                    p7 == adv and p8 == adv and p9 == adv:
                print('EU GANHEI!\n')
                pts_pc += 1
                vencedor = 'PC'
                turnos = 10

        def atualizar_tudo():
            global jogada
            global turnos
            global vencedor

            if primeiro == 'EU':
                rotina_j1()
                atualizar_jogadas_j1()
                atualizar_tabuleiro()
                checar_vencedor()

                if turnos == 5:
                    print('NÓS EMPATAMOS!\n')
                    turnos = 10
                    vencedor = 'EMPATE'

                if vencedor == '':
                    atualizar_jogadas_j2()
                    atualizar_tabuleiro()
                    checar_vencedor()

            elif primeiro == 'PC':
                atualizar_jogadas_j2()
                atualizar_tabuleiro()
                checar_vencedor()

                if turnos == 5:
                    print('NÓS EMPATAMOS!\n')
                    turnos = 10
                    vencedor = 'EMPATE'

                if vencedor == '':
                    rotina_j1()
                    atualizar_jogadas_j1()
                    atualizar_tabuleiro()
                    checar_vencedor()

            jogada = 0
            turnos += 1

        while turnos <= 5:
            atualizar_tudo()

        print('-------- PLACAR --------')
        print('Você: {} | Computador: {}'.format(pts_jogador, pts_pc))
        print('------------------------')

        while True:
            reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para não: ').lower()

            if reiniciar in ('s', 'n', '"s"', '"n"'):
                break
            print('\nResposta inválida!')

        if reiniciar == 's' or reiniciar == '"s"':
            print('\n-----------------------------------------------------')
            continue
        else:
            sys.exit(0)

def ex5():

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
                if all(cell == jogador for cell in linha[i:i + 4]):
                    return True

        # Verificar vitória na vertical
        for coluna in range(7):
            for i in range(3):
                if all(tabuleiro[i][coluna] == jogador for i in range(i, i + 4)):
                    return True

        # Verificar vitória na diagonal (ascendente)
        for i in range(3, 6):
            for j in range(4):
                if tabuleiro[i][j] == jogador and tabuleiro[i - 1][j + 1] == jogador and tabuleiro[i - 2][
                    j + 2] == jogador and tabuleiro[i - 3][j + 3] == jogador:
                    return True

        # Verificar vitória na diagonal (descendente)
        for i in range(3):
            for j in range(4):
                if tabuleiro[i][j] == jogador and tabuleiro[i + 1][j + 1] == jogador and tabuleiro[i + 2][
                    j + 2] == jogador and tabuleiro[i + 3][j + 3] == jogador:
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

    # Iniciar o jogo
    jogo_quatro_em_linha()



import random

def jogo_da_gloria():

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

                jogador1_posicao, permissao_jogador1 = processar_condiçoes_e_posicoes_dos_jogadores(jogador1_nome,
                                                                                                    jogador1_posicao)

                verificar_vitoria_jogadores(jogador1_nome, jogador1_posicao, jogador2_nome, jogador2_posicao)

                # realizacao_avancar_casas("Jogador1", "jogador2", f"{i}", True, f"{i}")

            else:
                permissao_jogador1 = True

            if permissao_jogador2:

                # Jogador 2 faz seus lançamentos
                jogador2_posicao += lancamentos_de_dados_dos_jogadores(jogador2_nome)

                jogador2_posicao, permissao_jogador2 = processar_condiçoes_e_posicoes_dos_jogadores(jogador2_nome,
                                                                                                    jogador2_posicao)

                verificar_vitoria_jogadores(jogador2_nome, jogador2_posicao, jogador2_nome, jogador2_posicao)

                # realizacao_avancar_casas("Jogador1", "jogador2", f"{i}", True, f"{i}")

            else:
                permissao_jogador2 = True


    def lancamentos_de_dados_dos_jogadores(jogador_nome):

        input(
            f"Olá {jogador_nome},para quiser fazer os lançamentos dos dois dados é preciso que você clique a tela Enter."
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

        return realizacao_avancar_casas("Jogador1" "jogador2", "{i}", True, "{i]")


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

        elif posicao_atual == 27:

            print(
                f"{jogador_nome}, você está na casa {posicao_atual}. Você calhou ter a casa partilha com outro jogador,"
                f"após do seu lançamentos em diante. Grande azar você calhou ")

            return

        else:
            return posicao_atual, True

    def verificar_vitoria_jogadores(jogador1_nome, jogador1_posicao, jogador2_nome, jogador2_posicao):

        if jogador1_posicao >= 50:

            print(f"Parabéns, {jogador1_nome}! Você venceu o jogo!")
            exit()  # Encerra o programa quando um jogador vence

        elif jogador2_posicao >= 50:
            print(f"Parabéns, {jogador2_nome}! Você venceu o jogo!")
            exit()  # Encerra o programa quando um jogador vence



    if __name__ == "__main__":
        jogoDaGloria()

