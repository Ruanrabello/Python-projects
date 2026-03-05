import sqlite3


def criar_banco():
    # Cria ou abre um banco de dados chamado 'banco.db'
    conexao = sqlite3.connect('banco.db')
    conexao.execute('PRAGMA foreign_keys = ON')  # Ativa restrições de FK

    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL no banco

    conexao.commit()  # Salva as alterações no banco
    conexao.close()   # Fecha a conexão com o banco


criar_banco()
