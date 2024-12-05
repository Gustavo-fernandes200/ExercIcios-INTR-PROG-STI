
import math

# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Lê as notas do aluno
nota_matematica = float(input("Digite a nota de matematica: "))
nota_portugues = float(input("Digite a nota de português: "))
nota_ingles = float(input("Digite a nota de inglês: "))
nota_geografia = float(input("Digite a nota de geografia: "))

# Calcula a média das notas
notas = [nota_matematica, nota_portugues, nota_ingles, nota_geografia]
media = calcular_media(notas)

# Verifica se o aluno foi aprovado ou reprovado
if media >= 9.5:
    print("Aprovado")

else:
    print("Reprovado")
