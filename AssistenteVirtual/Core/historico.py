import json  # ? importa biblioteca para salvar e carregar estruturas python em  JSON
import os  # ? Importa funçoes relacionadas ao sistema

CAMINHO_HISTORICO = "C:/Users/ruanb/Downloads/Docs/Assistente/data/Historico.json"


def carregar_historico():  # ? Carrega o historico do arquivo JSON
    # ? Verifica se o ficheiro data/historico.json existe. Se não existir, a função vai retornar uma lista vazia no final.
    if os.path.exists(CAMINHO_HISTORICO):
        try:
            # ? Abre o ficheiro em modo leitura ("r") com codificação UTF-8.
            with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


# ? recebe a lista historico e a grava no ficheiro JSON..
def salvar_historico(historico):
    # ? Abre o ficheiro em modo escrita ("w"),
    with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


# ? Adiciona nova mensagem ao historico.
def adicionar_mensagem(historico, role, content):
    # ? Acrescenta um dicionário com as chaves role e content à lista historico. Exemplo: {"role": "user", "content": "Olá"}.
    historico.append({"role": role, "content": content})

    if len(historico) > 50:  # ? Se o tamanho do histórico exceder 20 entradas,
        historico.pop(0)  # ? remove a primeira (mensagem mais antiga)

    salvar_historico(historico)
    return historico


def limpar_historico():  # ? Apaga todo o historico
    if os.path.exists(CAMINHO_HISTORICO):
        os.remove(CAMINHO_HISTORICO)
