import random

print("\n******************* Python JogoAdivinhacao *******************")


NumeroAleatorio = random.randint(1, 10)
tentativas = 5

while True:
    NumeroJogador = int(input("Digite um numero: "))

    if NumeroJogador == NumeroAleatorio:
        print("Acertou")
        break
    elif NumeroJogador > 10:
        print("Voce digitou um numero maior que o permitido")
        break
    else:
        print("TENTE NOVAMENTE")
        tentativas = tentativas - 1

        if tentativas == 0:
            print("ACABOU AS TANTATIVAS, O NUMERO CORRETO ERA {}".format(
                NumeroAleatorio))
            break
print("\n******************* FIM *******************")
