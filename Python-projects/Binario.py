def add_binary(a, b):
    resultado = a + b
    numero_binario = bin(resultado)[2:]
    print(f"A soma é: {resultado} e em números binários é: {numero_binario}")


print(add_binary(5, 9))
