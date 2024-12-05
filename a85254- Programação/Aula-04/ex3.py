"""
Implemente um programa que pesquise o número “valor” numa lista de N elementos.

"""
num_pesquisar = int(input("Introduz um numero para no qual pesquise numa lista de elementos : "))

lista = [4,5,6,7,8,9,10,36,635,4534,5235]

for num in lista :
    if num == num_pesquisar :
        print("O numero foi encontrado : ")
        break
