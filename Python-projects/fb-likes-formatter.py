def likes(names):
    Qtde_nomes = len(names)

    if Qtde_nomes == 3:
        return (f"{names[0]}, {names[1]} and {names[2]} like this")

    elif Qtde_nomes == 2:
        return (f"{names[0]} and {names[1]} like this")

    elif Qtde_nomes == 1:
        return (f"{names[0]} likes this")

    elif Qtde_nomes == 0:
        return ("no one likes this")

    else:
        numero = Qtde_nomes - 2
        return (f"{names[0]}, {names[1]} and {numero} others  like this")


print(likes(['Max', 'John', 'Mark']))


#🔹 Descrição:

# Implementação em Python de uma função que simula a exibição de curtidas no estilo do Facebook.
# A função adapta a frase conforme a quantidade de nomes na lista, exibindo desde "no one likes this" até "X and Y and Z others like this".