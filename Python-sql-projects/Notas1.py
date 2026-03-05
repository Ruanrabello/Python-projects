import sqlite3

# Função responsável por cadastrar uma nota para um aluno


def cadastra_notas(aluno_id, Nota):
    # Abre uma conexão com o banco de dados (coloque sempre o caminho completo se necessário)
    conexao = sqlite3.connect(
        r'C:\Users\ruanb\Downloads\cursos\EstudosProgramacao\Estudos\Python\Estudos\Projetos\Projeto.sql.python\banco.db'
    )

    # Ativa a verificação de chave estrangeira (garante que o aluno exista antes de inserir a nota)
    conexao.execute('PRAGMA foreign_keys = ON')

    try:
        cursor = conexao.cursor()
        # Insere a nota na tabela 'notas' associando ao ID do aluno
        cursor.execute(
            'INSERT INTO notas (aluno_id, nota) VALUES (?, ?)', (aluno_id, Nota))

        conexao.commit()  # Salva (confirma) as alterações no banco
        print(
            f'\n✅ A nota {Nota} pertencente ao aluno de ID {aluno_id} foi adicionada com sucesso!\n')

    except sqlite3.IntegrityError:
        # Mostra essa mensagem se o aluno_id não existir (por causa da chave estrangeira)
        print(
            f'\n❌ Erro: o aluno com ID {aluno_id} não existe. Nota não adicionada.\n')

    finally:
        conexao.close()  # Fecha a conexão com o banco (boa prática sempre fazer isso)


#! Parte principal do programa — só roda se o arquivo for executado diretamente
if __name__ == "__main__":
    print("\n\n---------------- Bem-vindo ao cadastro de notas ----------------\n")

    # * Loop para permitir vários cadastros até o usuário digitar 'sair'
    while True:
        # * Solicita a nota do aluno
        nota1 = input("Digite a nota do aluno (ou 'sair' para encerrar):\n")
        if nota1.lower() == 'sair':  # * Verifica se o usuário quer sair
            print("Encerrando o cadastro de notas.")
            break

        # 1 Solicita o ID do aluno
        identificacao = input("Digite o ID do aluno:\n")
        if identificacao.lower() == 'sair':  # Verifica novamente se o usuário quer sair
            print("Encerrando o cadastro de notas.")
            break

        try:
            # Converte os valores digitados para os tipos corretos
            nota1_float = float(nota1)      # Converte a nota para float
            id_int = int(identificacao)     # Converte o ID para inteiro

            # Chama a função para cadastrar a nota no banco
            cadastra_notas(id_int, nota1_float)

        except ValueError:
            # Mostra erro caso o usuário digite valores não numéricos
            print("❌ Entrada inválida! Digite uma nota (número) e um ID válido.\n")
