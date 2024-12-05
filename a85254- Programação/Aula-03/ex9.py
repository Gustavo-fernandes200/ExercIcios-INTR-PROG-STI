"""
Escreva o algoritmo e o programa para todos os estudantes do TeSP do ISE-DEE por
turma, ler (não use vetores e/ou matrizes e/ou strings):
(a) a idade;
(b) o género (masculino – 1; feminino – 0);
(c) nota de entrada.
Apresente:
(i) qual a turma com a aluno com o aluno mais novo
(ii) qual a turma com o aluno mais velho
(iii) quantas raparigas existem nos TeSP-DEE
(iv) qual a turma com o aluno com a nota de entrada mais alta
(v) qual a nota de entrada mais alta e o género da pessoa que teve essa nota
"""
# Inicialização de variáveis para a menor idade, maior idade, quantidade de raparigas,
# nota de entrada mais alta e género correspondente
menor_idade = float('inf')
turma_mais_nova = 0
maior_idade = 0
turma_mais_velha = 0
quantidade_raparigas = 0
turma_mais_raparigas = 0
turma_mais_raparigas_num = 0
nota_entrada_mais_alta = 0
turma_mais_alta = 0
genero_nota_alta = None

# Loop para cada turma

num_turmas = int(input("Digite o número de turmas: "))
for turma in range(num_turmas):

    # Entrada de dados

    idade = int(input(f"Turma {turma + 1} - Insira a idade do aluno: "))
    genero = int(input("Insira o género (masculino - 1; feminino - 0): "))
    nota_entrada = float(input("Insira a nota de entrada do aluno: "))

    # Atualização da menor idade e turma mais nova

    if idade < menor_idade:
        menor_idade = idade
        turma_mais_nova = turma + 1

    # Atualização da maior idade e turma mais velha

    if idade > maior_idade:
        maior_idade = idade
        turma_mais_velha = turma + 1

    # Contagem de raparigas e atualização da turma com mais raparigas

    if genero == 0:
        quantidade_raparigas += 1
        if quantidade_raparigas > turma_mais_raparigas:
            turma_mais_raparigas = quantidade_raparigas
            turma_mais_raparigas_num = turma + 1

    # Atualização da nota de entrada mais alta e género correspondente

    if nota_entrada > nota_entrada_mais_alta:
        nota_entrada_mais_alta = nota_entrada
        genero_nota_alta = "Feminino" if genero == 0 else "Masculino"
        turma_mais_alta = turma + 1

# Apresentação das informações solicitadas

print(f"A turma com o aluno mais novo é a turma {turma_mais_nova}.")
print(f"A turma com o aluno mais velho é a turma {turma_mais_velha}.")
print(f"Existem {quantidade_raparigas} raparigas nos TeSP-DEE na turma {turma_mais_raparigas_num}.")
print(f"A turma com o aluno com a nota de entrada mais alta é a turma {turma_mais_alta}.")
print(f"A nota de entrada mais alta foi {nota_entrada_mais_alta} e o género da pessoa com essa nota foi {genero_nota_alta}.")

