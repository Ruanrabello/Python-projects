import requests

# URL da API com cidade e chave
cidade = "Rio de Janeiro"
Chave_api = "50b8a81c9ba094c01b96f916916d2b35"
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={Chave_api}&lang=pt_br&units=metric"

# Fazendo requisição
resposta = requests.get(url)
dados = resposta.json()  # Agora com os parênteses

# Pegando informações específicas
temperatura = dados["main"]["temp"]
descricao = dados["weather"][0]["description"]
temperatura_minima = dados["main"]["temp_min"]
temperatura_maxima = dados["main"]["temp_max"]


# Mostrando o resultado
print(f"🌞 {cidade} - {temperatura}°C - {descricao.capitalize()}")
print(f"🔹 Temperatura minima: {temperatura_minima}°C")
print(f"🔸 Temperatura maxima: {temperatura_maxima}°C")


# print(dados)
