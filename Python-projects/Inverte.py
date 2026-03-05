def invertido(frase):
    lst = frase.split()
    resultado = []

    for palavra in lst:
        if len(palavra) > 5:
            palavra = palavra[::-1]  # inverte as letras
        resultado.append(palavra)

    return ' '.join(resultado)


print(invertido("Hey fellow warriors"))
