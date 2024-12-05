def main():
    nome_completo_apelido = input("Me diga seu primeiro nome e seu apelido : ")
    nome_ajustado_medida = organizacao_apelido(nome_completo_apelido)
    print("Já está concluido a modificação a pedido por você :", nome_ajustado_medida)

def organizacao_apelido(nome_completo_apelido):
    apelido = nome_completo_apelido.split()
    sobrenome = apelido[-1]
    primeiro_nome = " ".join(apelido[:1])
    nome_ajustado_medida = sobrenome + ", " + primeiro_nome
    return nome_ajustado_medida


main()
