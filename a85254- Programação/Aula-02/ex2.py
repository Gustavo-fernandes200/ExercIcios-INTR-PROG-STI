import random
import math

# Dá coeficientes aleatórios para a equação de segundo grau
a = random.randint(0, 10)
b = random.randint(5, 20)
c = random.randint(5, 20)

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica se existem raízes reais
if delta < 0:
    print("Não existem raízes reais.")
else:
    # Calcula as raízes usando a fórmula resolvente
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Raiz 1:", x1)
    print("Raiz 2:", x2)
