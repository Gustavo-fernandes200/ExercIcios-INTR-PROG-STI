
import random

def jogo_da_forca():
    print("Bem-vindos ao Jogo da Forca!")

    jogador1 = input("Digite o nome do Jogador 1: ")
    categoria_escolhida = escolha_categoria()

    print(f"\n{jogador1}, agora é a vez do Jogador 2.")
    jogador2 = input("Digite o nome do Jogador 2: ")

    print(f"\n{jogador1} e {jogador2}, preparem-se para a batalha!")

    palavra_secreta_jogador1 = escolher_palavra(categoria_escolhida)
    letras_certas_jogador1 = ['_'] * len(palavra_secreta_jogador1)
    letras_erradas_jogador1 = []
    tentativas_jogador1 = 6

    palavra_secreta_jogador2 = escolher_palavra(categoria_escolhida)
    letras_certas_jogador2 = ['_'] * len(palavra_secreta_jogador2)
    letras_erradas_jogador2 = []+
    tentativas_jogador2 = 6

    while True:
        print(f"\n{ jogador1.upper() }:")
        exibir_estado_jogo(palavra_secreta_jogador1, letras_certas_jogador1, letras_erradas_jogador1, tentativas_jogador1)

        letra_jogador1 = obter_letra()
        revelar_letras(palavra_secreta_jogador1, letras_certas_jogador1, letras_erradas_jogador1, letra_jogador1)

        if not tentativas_jogador1 or '_' not in letras_certas_jogador1:
            break

        print(f"\n{ jogador2.upper() }:")
        exibir_estado_jogo(palavra_secreta_jogador2, letras_certas_jogador2, letras_erradas_jogador2, tentativas_jogador2)

        letra_jogador2 = obter_letra()
        revelar_letras(palavra_secreta_jogador2, letras_certas_jogador2, letras_erradas_jogador2, letra_jogador2)

        if not tentativas_jogador2 or '_' not in letras_certas_jogador2:
            break

    print(f"\n{ jogador1.upper() }:")
    exibir_resultado_final(palavra_secreta_jogador1, letras_certas_jogador1)

    print(f"\n{ jogador2.upper() }:")
    exibir_resultado_final(palavra_secreta_jogador2, letras_certas_jogador2)


def exibir_menu_categorias():
    print("Escolha a categoria temática:")
    categorias = ["frutas", "países", "animais", "profissões", "tecnologia", "objetos", "cores", "esportes",
                  "carros", "instrumentos_musicais", "filmes", "frutas_exóticas", "capitais", "idiomas",
                  "instrumentos_científicos", "elementos_químicos", "flores", "distritos_portugueses",
                  "cidades_portuguesas", "comidas", "instrumentos_de_percussão", "constelações",
                  "instrumentos_de_corda", "instrumentos_de_sopro", "especialidades_médicas",
                  "lugares_fantásticos", "gêneros_musicais", "instrumentos_virtuais", "programas_de_tv",
                  "marcas_de_carro"]

    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")


def escolha_categoria(categorias=None):
    if categorias is None:
        categorias = ["frutas", "países", "animais", "profissões", "tecnologia", "objetos", "cores", "esportes",
                      "carros", "instrumentos_musicais", "filmes", "frutas_exóticas", "capitais", "idiomas",
                      "instrumentos_científicos", "elementos_químicos", "flores", "distritos_portugueses",
                      "cidades_portuguesas", "comidas", "instrumentos_de_percussão", "constelações",
                      "instrumentos_de_corda", "instrumentos_de_sopro", "especialidades_médicas",
                      "lugares_fantásticos", "gêneros_musicais", "instrumentos_virtuais", "programas_de_tv",
                      "marcas_de_carro"]

    exibir_menu_categorias()

    opcao = input("Digite o número correspondente à categoria desejada (ou deixe em branco para escolha aleatória): ")

    if opcao.isdigit() and 1 <= int(opcao) <= len(categorias):
        return categorias[int(opcao) - 1]
    else:
        return random.choice(categorias)


def escolher_palavra(categoria):
    palavras_temas = {
        "frutas": ["banana", "maçã", "uva", "abacaxi", "manga", "melancia", "morango", "kiwi", "pêssego", "laranja"],

        "países": ["brasil", "alemanha", "japão", "canadá", "austrália", "itália", "frança", "méxico", "índia", "egito"],

        "animais": ["leão", "elefante", "girafa", "tigre", "panda", "gato", "cachorro", "papagaio", "macaco", "peixe"],

        "profissões": ["médico", "engenheiro", "professor", "chef", "piloto", "advogado", "arquiteto", "jornalista",
                       "músico", "cientista"],

        "tecnologia": ["computador", "internet", "programação", "inteligência artificial", "criptografia", "smartphone",
                       "robótica", "realidade virtual", "cibersegurança", "big data"],

        "objetos": ["abre-latas", "âncora", "aquecedor", "armadura", "bandeira", "bacia", "bisturi", "borracha",
                    "bengala", "bandeira", "balança", "binóculo", "cadeira", "caneta", "carteira", "escova", "espelho",
                    "faca", "garfo", "guarda-chuva"],

        "cores": ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "marrom", "rosa", "cinza", "preto"],

        "esportes": ["futebol", "basquete", "natação", "vôlei", "atletismo", "tênis", "ciclismo", "boxe", "golfe",
                     "hóquei"],

        "carros": ["civic", "corolla", "mustang", "camaro", "fusca", "bmw", "mercedes", "tesla", "fiat", "volvo"],

        "instrumentos_musicais": ["violino", "piano", "guitarra", "trompete", "bateria", "flauta", "saxofone",
                                  "violoncelo", "trombone", "clarinete"],

        "filmes": ["avatar", "star wars", "titanic", "matrix", "inception", "harry potter", "forrest gump",
                   "the godfather", "the shawshank redemption", "jurassic park"],

        "frutas_exóticas": ["pitaya", "kiwano", "rambutan", "mangostão", "carambola", "sapote", "longan", "durian",
                            "jabuticaba", "cherimoya"],

        "capitais": ["brasília", "berlim", "tóquio", "ottawa", "canberra", "lisboa", "paris", "roma", "madrid",
                     "amsterdã"],

        "idiomas": ["português", "inglês", "espanhol", "francês", "chinês", "alemão", "italiano", "russo", "japonês",
                    "árabe"],

        "instrumentos_científicos": ["microscópio", "telescópio", "espectrômetro", "cromatógrafo", "higrômetro",
                                     "termômetro", "centrífuga", "microscópio eletrônico", "pipeta", "bureta"],

        "elementos_químicos": ["hidrogênio", "oxigênio", "carbono", "ouro", "ferro", "urânio", "cobre", "alumínio",
                               "prata", "chumbo"],

        "flores": ["rosa", "girassol", "orquídea", "lírio", "margarida", "tulipa", "cravo", "violeta", "camélia",
                   "azaleia"],

        "distritos_portugueses": ["lisboa", "porto", "braga", "aveiro", "setúbal", "coimbra", "leiria", "santarém",
                                  "faro", "viseu"],

        "cidades_portuguesas": ["lisboa", "porto", "braga", "aveiro", "coimbra", "funchal", "guarda", "evora", "beja",
                                "viana do castelo"],

        "comidas": ["pizza", "sushi", "hambúrguer", "lasanha", "tacos", "risoto", "paella", "kebab", "ramen", "cuscuz"],

        "instrumentos_de_percussão": ["tambor", "bongô", "conga", "marimba", "caixa", "pratos", "ganzá", "triângulo",
                                      "pandeiro", "surdo"],

        "constelações": ["órion", "ursa maior", "cassiopeia", "cão maior", "escorpião", "aquário", "andromeda", "taurus", "draco", "pegasus"],

        "instrumentos_de_corda": ["violão", "contrabaixo", "harpa", "cítara", "bandolim", "banjo", "ukulele", "viola",
                                  "guitarra elétrica", "violino"],

        "instrumentos_de_sopro": ["trompa", "trompete", "saxofone", "clarinete", "flauta transversal", "oboé", "fagote",
                                  "tuba", "trombone", "flautim"],

        "especialidades_médicas": ["cardiologia", "ortopedia", "dermatologia", "psiquiatria", "ginecologia", "urologia",
                                   "neurologia", "pediatria", "oncologia", "endocrinologia"],

        "lugares_fantásticos": ["atlântida", "el dorado", "shangri-la", "agarta", "avalon", "hibernia", "hyperborea",
                                "mu", "valhalla", "zion"],

        "gêneros_musicais": ["rock", "pop", "hip-hop", "jazz", "reggae", "samba", "funk", "blues", "country",
                             "eletrônica"],

        "instrumentos_virtuais": ["controlador midi", "teclado virtual", "guitarra elétrica virtual",
                                  "bateria eletrônica", "sintetizador", "violino virtual", "flauta virtual",
                                  "piano virtual", "controlador de DJ", "harpa virtual"],

        "programas_de_tv": ["breaking bad", "game of thrones", "stranger things", "the office", "friends",
                            "the simpsons", "the wire", "the sopranos", "westworld", "black mirror"],

        "marcas_de_carro": ["toyota", "honda", "ford", "chevrolet", "bmw", "mercedes-benz", "tesla", "volkswagen",
                            "audi", "nissan"]

    }

    return random.choice(palavras_temas[categoria])

def obter_letra():
    letra = input("Digite uma letra: ").lower()

    while not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite uma única letra válida.")
        letra = input("Digite uma letra: ").lower()

    return letra


def revelar_letras(palavra_secreta, letras_certas, letras_erradas, letra):
    if letra in palavra_secreta and letra not in letras_certas:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                letras_certas[i] = letra
    else:
        letras_erradas.append(letra)
        print(f"Incorreto! Você tem {6 - len(letras_erradas)} tentativa(s) restante(s).")


def exibir_estado_jogo(palavra_secreta, letras_certas, letras_erradas, tentativas):
    print("\nPalavra: ", " ".join(letras_certas))
    exibir_forca(len(letras_erradas))

    if letras_erradas:
        print("Letras erradas:")
        exibir_tabela(letras_erradas)

    print(f"Tentativas restantes: {tentativas}")


def exibir_resultado_final(palavra_secreta, letras_certas):
    print("\nResultado Final:")
    if '_' not in letras_certas:
        print(f"Parabéns! A palavra era: {palavra_secreta}")
    else:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")

    print("Obrigado por jogar!")


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
          /|\  |
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

