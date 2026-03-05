
import sqlite3


def cadastrar_aluno(nome):
    conexao = sqlite3.connect(
        r'C:\Users\ruanb\Downloads\cursos\EstudosProgramacao\Estudos\Python\Estudos\Projetos\Projeto.sql.python\banco.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO alunos (nome) VALUES (?)', (nome,))
    conexao.commit()
    conexao.close()
    print(f'Aluno "{nome}" cadastrado com sucesso!')


if __name__ == "__main__":
    #!resumidamente isso impede que se vc importar esse arquivo (como se fosse uma biblioteca) igual ta fazendo com o sqlite, rode isso aqui embaixo, isso so vai rodar sew vc executar esse arquivo aqui(cadastro.py) pra caso importe para outro e queira usar so a funcao
    #!if __name__ == "__main__": impede que esse trecho do código rode automaticamente quando você importa o arquivo como se fosse uma biblioteca.

    #!Ou seja: só vai rodar o que está dentro dele se você executar diretamente o arquivo (ex: python cadastro.py).
    # !Isso é útil quando você quer importar funções de outro arquivo (como cadastrar_aluno) sem rodar inputs, prints ou menus sem querer.
    print("\n\n----------------Bem vindo ao cadastro de alunos e notas-------------\n\n")

    while True:

        nome = input("Digite o nome do aluno (ou 'sair' para encerrar):\n")
        if nome.lower() == 'sair':  # * Verifica se o usuário quer sair
            print("Encerrando o cadastro de notas.")
            break

        try:
            nome_str = str(nome)

            cadastrar_aluno(nome_str)

        except ValueError:
            # Mostra erro caso o usuário digite valores não numéricos
            print("❌ Entrada inválida! Tente Novamente\n")
