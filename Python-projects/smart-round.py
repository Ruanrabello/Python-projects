import math


def round_it(n):
    numero_string = str(n)

    # 1 verificar se tem parte decimal
    if "." in numero_string:
        parte_decimal = numero_string.split(".")[1]
        parte_nao_decimal = numero_string.split(".")[0]
        qtd_digitos_nao_decimais = len(parte_nao_decimal)
        qtd_digitos_decimais = len(parte_decimal)

    else:
        # se for inteiro, considera como "0 dígitos decimais"
        qtd_digitos_decimais = 0
        qtd_digitos_nao_decimais = len(numero_string)
        numero_inteiro = numero_string

    if qtd_digitos_decimais > qtd_digitos_nao_decimais:
        return math.ceil(n)
    elif qtd_digitos_decimais < qtd_digitos_nao_decimais:
        return math.floor(n)
    else:
        return round(n)


print(round_it(3.425))   # 4
print(round_it(34.5))   # 34
print(round_it(34.56))  # 35

#🔹 Descrição:

# Função personalizada em Python para arredondamento inteligente de números.
#O algoritmo compara a quantidade de dígitos antes e depois da vírgula para decidir se deve aplicar math.ceil, math.floor ou round, tornando o arredondamento mais adaptável a diferentes cenários.