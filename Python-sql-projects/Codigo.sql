-- Criar tabela quarto
CREATE TABLE IF NOT EXISTS alunos (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     NOME TEXT NOT NULL                
);

--CRIAR TABELA NOTAS
CREATE TABLE notas (
    id integer PRIMARY KEY AUTOINCREMENT,
    aluno_id integer,
    nota REAL,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id)
);


--VISUALIZAR
SELECT * FROM alunos
SELECT * FROM notas 

--DELETAR
DELETE FROM alunos WHERE ID IN (1,2,3,4,5,6,7,8,9);
DELETE FROM NOTAS WHERE ID IN (5,6,7);

--OU
DELETE FROM alunos WHERE ID = 6







-- O ALUNO_CPF E UMA CHAVE ESTRANGEIRA QUE ESTA VINDO DE OUTRA TABELA, ENTAO NO FINAL VC COLOCA QUAL E A COLUNA ESTRANGEIRA, E DA REFERENCIA DE QUAL TABELA ELA ESTA VINDO E QUAL COLUNA ELA E, PQ ASSIMGARANTE QUE SO HAJA NOTA SE ANTESZ OUBVER ALUNO
--O campo aluno_cpf na tabela de notas é uma chave estrangeira, ou seja, ele depende de outro campo que está na tabela de alunos (o cpf).
--Isso garante que só existirá uma nota se o aluno já estiver cadastrado.

