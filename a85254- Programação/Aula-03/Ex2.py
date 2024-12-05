# Definir e dando os valores dos x e y
x1 = 1
y1 = 1

x2 = 2
y2 = 2

# Fazendo o import necessecial
import math

# Função para calculator a distância entre os dois pontos
def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
    return distancia

# Obtendo as coordenadas dos pontos do usuário
x1 = float(input("Introduza a coordenada x1 do primeiro ponto: "))
y1 = float(input("Introduza a coordenada y1 do primeiro ponto: "))
x2 = float(input("Introduza a coordenada x2 do segundo ponto: "))
y2 = float(input("Introduza a coordenada y2 do segundo ponto: "))

# Calculando e exibindo a distância entre os dois pontos
distancia = calcular_distancia(x1, y1, x2, y2)
print(f'A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {distancia}')
