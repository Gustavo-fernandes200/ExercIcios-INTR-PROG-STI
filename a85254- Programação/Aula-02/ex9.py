"""
Implemente um programa para calcular:
    (a) a média das idades e das alturas de todos os alunos da turma;
    (b) qual a altura do aluno mais alto
    (c) qual a idade do aluno mais novo
"""

# Inicializa variáveis para armazenar a soma das idades e alturas, altura do aluno mais alto e idade do aluno mais novo
soma_idades = 0
soma_alturas = 0
altura_aluno_mais_alto = 0
idade_aluno_mais_novo = float('inf')  # Inicializa com um valor grande para garantir que qualquer idade será menor

# Solicita o número de alunos na turma
num_alunos = int(input("Digite o número de alunos na turma: "))

# Loop para ler as idades e alturas dos alunos
for i in range(num_alunos):
    idade = int(input("Digite a idade do aluno: "))
    altura = float(input("Digite a altura do aluno (em metros): "))

    # Atualiza a soma das idades e alturas
    soma_idades += idade
    soma_alturas += altura

    # Verifica se a altura é a maior até agora
    if altura > altura_aluno_mais_alto:
        altura_aluno_mais_alto = altura

    # Verifica se a idade é a menor até agora
    if idade < idade_aluno_mais_novo:
        idade_aluno_mais_novo = idade

# Calcula a média das idades e alturas
media_idades = soma_idades / num_alunos
media_alturas = soma_alturas / num_alunos

# Exibe os resultados
print(f"A média das idades dos alunos é: {media_idades:.2f} anos")
print(f"A média das alturas dos alunos é: {media_alturas:.2f} metros")
print(f"A altura do aluno mais alto é: {altura_aluno_mais_alto:.2f} metros")
print(f"A idade do aluno mais novo é: {idade_aluno_mais_novo} anos")
