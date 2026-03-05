import sqlite3


def mostrar_notas_alunos():
    conexao = sqlite3.connect(
        r'C:\Users\ruanb\Downloads\cursos\EstudosProgramacao\Estudos\Python\Estudos\Projetos\Projeto.sql.python\banco.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT alunos.NOME, AVG(notas.nota) as media from alunos
                      left join notas on alunos.id = notas.aluno_id
                      group by alunos.id;   
 ''')

    alunos = cursor.fetchall()
    print("\nNotas e médias dos alunos:\n")
    for nome, media in alunos:
        if media is not None:
            print(f'Aluno: {nome} | Média: {media:.2f}')
        else:
            print(f'Aluno: {nome} | Sem notas registradas')

    conexao.close()


'''-----------------------------------------------'''


if __name__ == "__main__":
    mostrar_notas_alunos()


# ? Está escrito alunos.nome porque:
# ! - "alunos" é o nome da tabela
# ! - "nome" é o nome da coluna
# ! Usamos tabela.coluna quando há mais de uma tabela para evitar confusão

# ? LEFT JOIN notas ON alunos.id = notas.aluno_id
# ! - alunos.id → chave primária da tabela alunos
# ! - notas.aluno_id → chave estrangeira da tabela notas, que aponta para o ID do aluno
#!--- Junte a tabela alunos com a tabela notas, relacionando o id do aluno com o aluno_id da nota---

# ? GROUP BY alunos.id – O que faz isso?
# ! Agrupa os dados por aluno (pelo ID)
# ! É necessário quando queremos fazer cálculos por aluno, como média, soma, etc.

# ? alunos = cursor.fetchall()
# ! fetchall() retorna uma lista de tuplas com os resultados da consulta SQL
#!(RUAN, 4)

# ? Por que usar AVG se já tenho GROUP BY?
# ! O GROUP BY só agrupa os dados
# ! O AVG é quem realmente calcula a média
# ! Se você não usar AVG, o SQL pega qualquer valor do grupo (não confiável)

# ? O que é essa variável 'media'?
# ! É uma variável Python que guarda o valor da média retornada pela consulta SQL

# ? Mas eu achei que AVG calculava a média da turma, não individual
# ! Correto! Sozinho, AVG calcula a média geral
# ! Quando usamos AVG + GROUP BY, ele calcula a média de cada grupo (no caso, de cada aluno)
