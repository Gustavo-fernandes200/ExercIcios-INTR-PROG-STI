"""
Escreva o algoritmo e o programa para fazer a factoração de um número inteiro
(fatorar é o mesmo que decompor o número em fatores primos, isto é, escrever um
número através da multiplicação de números primos. Na fatoração utilizamos os
números primos obedecendo a uma ordem crescente de acordo com as regras de
divisibilidade em razão do termo a ser fatorado. Números primos são aqueles que
podem ser divididos somente por um e por ele mesmo. Observe a decomposição em
fatores primos dos números a seguir:

24 = 2 x 2 x 2 x 3
10 = 2 x 5
52 = 2 x 2 x 13
112 = 2 x 2 x 2 x 2 x 7
600 = 2 x 2 x 2 x 3 x 5 x 5

Forma prática de factoração:
O número a ser fatorado deverá ocupar a coluna da esquerda e a coluna da direita será preenchida com os fatores primos. Ao dividir o
número pelo algarismo primo os resultados deverão ser colocados na coluna da direita.
As divisões deverão ser efetuadas no intuito de simplificar ao máximo o número, isto é
reduzi-lo ao número 1).

"""
num = int(input(" Numero para factoração : "))

num_original = num

while True:
    for i in range(2, num_original + 1):
        if num % i == 0:
            num /= i
            print(i,end="x")
            break

    if num == 1:
        print("\b")
        break

