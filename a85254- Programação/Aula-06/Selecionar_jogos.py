
from ex4 import jogo_do_galo
from ex5 import jogo_quatro_em_linha
from jogo_da_gloria import jogoDaGloria

def main():

    while True:

        print("\nEscolha um jogo:")
        print("a) Jogo do Galo")
        print("b) Jogo 4 em Linha")
        print("c) Jogo da Glória")
        print("ENCERRAR) Sair")

        escolha = input("Digite a opção desejada: ")

        if escolha == 'a':
            jogo_do_galo()

        elif escolha == 'b':
            jogo_quatro_em_linha()

        elif escolha == 'c':
            jogoDaGloria()

        elif escolha == 'ENCERRAR':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
