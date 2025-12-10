# ? Importa o modulu que permite que o python abra urls no navegador, como youtube etc
import webbrowser
import datetime  # ? módulo de data/hora
import os  # ? módulo do sistema operacional


def abrir_youtube():
    webbrowser.open("https://www.youtube.com/")


def abrir_google():
    webbrowser.open("https://www.google.com.br/index.html")


def dizer_hota():  # ? pega a hora atual e retorna uma string formatada.
    # ?  retorna um objeto datetime com data e hora atuais e converte esse objeto em uma str formatada, %H = hora com 2 dígitos, %M = minuto com 2 dígitos
    agora = datetime.datetime.now().strftime("%H:%M")
    return (f"Agora são {agora}")


# ? sbre um programa no Windows pelo caminho completo.
def abir_programa(caminho):
    try:
        os.startfile(caminho)
    except Exception as e:
        # ? classe base de praticamente todos os erros em Python, lasse base de praticamente todos os erros em Python
        return (f"Erro ao abrir o programa: {e}")


# ? Detecta comandos simples no texto do usuário e retorna uma ação.
def interpretar_comando(texto):
    texto = texto.lower()

    if "youtube" in texto:
        abrir_youtube()
        return ("Abrindo Youtube...")
    elif "google" in texto:
        abrir_google()
        return ("Abrindo Google...")
    elif "hora" in texto:
        return dizer_hota()
    elif "calculadora" in texto:
        abir_programa("C:\\Windows\\System32\\calc.exe")
        return ("Abrindo Calculadora")

    return None
