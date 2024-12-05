# Inicializar variáveis para armazenar o nome e a idade da pessoa mais nova
nome_mais_novo = None
idade_mais_nova = int(999)  # Inicializada com um valor infinitamente grande

# Loop para ler informações sobre as pessoas
while True:
    # Entrada do número do Cartão de Cidadão (ou '999' para sair)
    numero_cc = input("Digite o número do Cartão de Cidadão (pressione 999 para sair ): ")

    # Verificar se o usuário deseja sair
    if numero_cc == '999':
        break

    # Entrada do nome e idade da pessoa
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    # Verificar se a pessoa é a mais nova até agora
    if idade < idade_mais_nova:
        nome_mais_novo = nome
        idade_mais_nova = idade

# Mostrar o nome e idade da pessoa mais nova
if nome_mais_novo is not None:
    print(f"A pessoa mais nova é {nome_mais_novo} com {idade_mais_nova} anos de idade.")
else:
    print("Nenhuma pessoa foi inserida.")
