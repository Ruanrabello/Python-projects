import pyttsx4
import speech_recognition as sr
import time  # Para o atraso

# Inicializadores
reconhecedor = sr.Recognizer()
sintetizador = pyttsx4.init('sapi5')
sintetizador.setProperty('rate', 220)
sintetizador.setProperty('volume', 1.0)

voices = sintetizador.getProperty('voices')
sintetizador.setProperty('voice', voices[0].id)


def falar_texto(texto):
    """Converte texto em voz com pequeno atraso para garantir reprodução."""
    if not texto.strip():
        return

    try:
        time.sleep(1)  # Pausa de 1 segundo antes de falar
        sintetizador.say(texto)
        sintetizador.runAndWait()  # Bloqueante: espera terminar
    except Exception as e:
        print(f"❌ Erro ao falar: {e}")


def ouvir_microfone():
    with sr.Microphone() as mic:
        print("🎤 Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(mic, duration=1)
        audio = reconhecedor.listen(mic)

    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("❌ Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Erro no serviço de reconhecimento: {e}")
        return ""
