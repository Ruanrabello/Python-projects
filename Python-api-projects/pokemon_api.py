import requests

# URL da API com nome e chave
nome_pokemon = input("Digite o nome do pokemon:")
url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"


# Fazendo requisição
resposta = requests.get(url)
dados = resposta.json()

# Pegando informações específicas
nome = dados["name"]
tipo = dados["types"][0]["type"]["name"]
altura = dados["weight"]
vida = dados["stats"][0]["base_stat"]


print("\n --------------------POKEDEX DO RUAN---------------------\n\n")
print(f"🔴Nome: {nome}")
print(f"🟡Tipo: {tipo}")
print(f"🟢Altura: {altura}Cm")
print(f"🟣Vida: {vida}Hp")
