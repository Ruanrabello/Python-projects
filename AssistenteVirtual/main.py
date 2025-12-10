from Core.voz import ouvir_microfone, falar_texto
from Core.ia import chamar_ia
from Core.comandos import interpretar_comando
from Core.historico import carregar_historico, adicionar_mensagem

# ? Hisótico da conversa
historico = carregar_historico()

print("🤖 Assistente iniciado. Diga 'PARAR' para encerrar.")

# ? Loop infinito que mantém o assistente escutando até receber o comando de encerrar (break).
while True:

    # ? Ouvir o usuário.
    # ? Chama a função eque pega oque vc fala e retorna o texto transcrito(string) e associa a variavel
    comando = ouvir_microfone()
    if comando == "":
        # ? Se a função retorna "", então continue reinicia o loop sem processar nada.
        continue

    # ? Comando de encerramento
    # ? Se ele indenticar parar no que o usuario falar, ele interrompe o loop com o break e chama a função que converte texto em voz.
    if "parar" in comando.lower():
        falar_texto("Encerrando a assitente. até mais amigo!")
        break

    # ? Verificar se é comando direto
    # ? Ele chama função que abre as urls e apps de acordo com a palavra chave q a gente fala, se a funçlãoindetificar a palavra chave vai abrir, exemplo o youtube
    resposta_comando = interpretar_comando(comando)
    if resposta_comando:
        # ? e vai retornar um texto (Exemplo: ("Abrindo Youtube..."))
        falar_texto(resposta_comando)
        continue

    # ? Se não for comando direto, enviar para a IA
    # ? Vai adicionar assim no meu historico.json  historico.append({"role": "user", "content": comando}), comando é oque eu falei
    adicionar_mensagem(historico, "user", comando)
    resposta_ia = chamar_ia(comando, historico)
    # ? e depois vai adicionar nese formato porema  resposta da ia
    adicionar_mensagem(historico, "assistant", resposta_ia)

    # ? Falar a respsota da IA
    falar_texto(resposta_ia)
