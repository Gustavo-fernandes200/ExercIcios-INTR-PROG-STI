
def leitura_disciplinas(disclipina):
    leitura = 'Programação Orientada Objetos'
    letras = leitura.split()
    acronimo = ""
    for palavra in letras:
        acronimo += palavra[0]
    return acronimo

# Chamada da função

disclipina = input("Introduza o nome da disclipina :")

nota = float(input("introduza a nota da disclipina:"))

print(leitura_disciplinas(disclipina), " - ", nota)