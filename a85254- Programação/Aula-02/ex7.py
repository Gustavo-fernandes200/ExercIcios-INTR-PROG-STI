# Solicita a entrada do usuário
entrada = input("Digite 'L' para ligar, 'D' para desligar ou 'F' para furar: ").upper()

# Verifica a entrada e exibe a mensagem correspondente
if entrada == 'L':
    print("Ligar")
elif entrada == 'D':
    print("Desligar")
elif entrada == 'F':
    print("Furar")
else:
    print("Entrada inválida. Por favor, digite 'L', 'D' ou 'F'.")
