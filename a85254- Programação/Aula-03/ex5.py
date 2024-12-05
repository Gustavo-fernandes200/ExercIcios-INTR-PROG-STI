# Lê os limites predefindos indicados
limit_highest = int(input("Digite o limite mais alto possível: "))
limit_lowest = int(input("Digite o limite mais baixo possível: "))

sum = 0

for i in range(limit_lowest,limit_highest + 1):
    sum = sum + i
print(sum)
