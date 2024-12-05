import random


def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!")
    jogador1 = input("Digite o nome do Jogador 1: ")

    escolha_ia = input("Deseja jogar contra a IA? (S/N): ").lower()
    if escolha_ia == 's':
        jogador2 = "IA"
    else:
        jogador2 = input("Digite o nome do Jogador 2: ")

    print(f"\n{jogador1} e {jogador2}, preparem-se para a batalha!")

    categoria = escolha_categoria()

    palavra_secreta = escolher_palavra(categoria)
    letras_certas = ['_'] * len(palavra_secreta)
    letras_erradas = []
    tentativas = 6

    while True:
        exibir_estado_jogo(palavra_secreta, letras_certas, letras_erradas, tentativas)

        if not tentativas or '_' not in letras_certas:
            break

        letra = obter_letra()
        revelar_letras(palavra_secreta, letras_certas, letras_erradas, letra)

        if not tentativas or '_' not in letras_certas:
            break

        if jogador2 == "IA":
            letra_ia = escolher_letra_ia(palavra_secreta, letras_certas, letras_erradas)
        else:
            letra_ia = obter_letra()
        revelar_letras(palavra_secreta, letras_certas, letras_erradas, letra_ia)

    exibir_resultado_final(palavra_secreta, letras_certas)

    print("\nObrigado por jogar!")


def escolha_categoria():
    print("Escolha a categoria temática:")
    print("1. Frutas")
    print("2. Países")
    print("3. Animais")
    print("4. Profissões")
    print("5. Tecnologia")
    print("6. Objetos")

    opcao = input("Digite o número correspondente à categoria desejada (ou deixe em branco para escolha aleatória): ")

    categorias = ["frutas", "países", "animais", "profissões", "tecnologia", "objetos"]

    if opcao.isdigit() and 1 <= int(opcao) <= 6:
        return categorias[int(opcao) - 1]
    else:
        return random.choice(categorias)


def escolher_letra_ia(palavra_secreta, letras_certas, letras_erradas):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letra_ia = random.choice(alfabeto)

    while letra_ia in letras_certas or letra_ia in letras_erradas:
        letra_ia = random.choice(alfabeto)

    return letra_ia


def escolher_palavra(categoria):
    palavras_temas = {
        "frutas": ["banana", "maçã", "uva", "abacaxi", "manga"],
        "países": ["brasil", "alemanha", "japão", "canadá", "austrália"],
        "animais": ["leão", "elefante", "girafa", "tigre", "panda"],
        "profissões": ["médico", "engenheiro", "professor", "chef", "piloto"],
        "tecnologia": ["computador", "internet", "programação", "inteligência artificial", "criptografia"],
        "objetos": ["abre-latas", "âncora", "aquecedor", "armadura", "bandeira"],
    }

    return random.choice(palavras_temas[categoria])


def obter_letra():
    letra = input("Digite uma letra: ").lower()

    while not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite uma única letra válida.")
        letra = input("Digite uma letra: ").lower()

    return letra


def revelar_letras(palavra_secreta, letras_certas, letras_erradas, letra):
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_certas[i] = letra
    else:
        letras_erradas.append(letra)
        print(f"Incorreto! Você tem {6 - len(letras_erradas)} tentativa(s) errada(s) restante(s).")


def exibir_estado_jogo(palavra_secreta, letras_certas, letras_erradas, tentativas):
    print("\nPalavra: ", " ".join(letras_certas))
    exibir_forca(len(letras_erradas))
    if letras_erradas:
        print("Letras erradas:")
        exibir_tabela(letras_erradas)
    print(f"Tentativas restantes: {6 - len(letras_erradas)}")


def exibir_resultado_final(palavra_secreta, letras_certas):
    print("\nResultado Final:")
    if '_' not in letras_certas:
        print(f"Parabéns! A palavra era: {palavra_secreta}")
    else:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")


def exibir_tabela(letras_erradas):
    print("+-----------------+")
    print("| Letras Erradas  |")
    print("+-----------------+")
    for letra in letras_erradas:
        print(f"| {letra}", end=" " * (17 - len(letra)))
        print("|")
    print("+-----------------+")


def exibir_forca(tentativas_incorretas):
    forca_visual = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\ |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]
    print(forca_visual[tentativas_incorretas])


if __name__ == "__main__":
    jogo_da_forca()
