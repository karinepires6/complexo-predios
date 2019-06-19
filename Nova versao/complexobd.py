import sqlite3

#Criando Schema 'complexo'
conn = sqlite3.connect('complexo.db')
cursor = conn.cursor()

print("Opened database successfully")
'''
conn.execute("""
CREATE TABLE usuario(
    id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);
""")

conn.execute("""
CREATE TABLE predio(
    id_predio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    capacidade_predio INTEGER NOT NULL
);
""")


conn.execute("""
CREATE TABLE andar(
    id_andar INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_predio INTEGER NOT NULL,
    capacidade_andar INTEGER NOT NULL,
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio)
);
""")

conn.execute("""
CREATE TABLE permissao_complexo(
    id_usuario INTEGER NOT NULL,
    tipo_usuario VARCHAR(50) NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
);
""")

conn.execute("""
CREATE TABLE permissao_predio(
    id_usuario INTEGER NOT NULL,
    id_predio INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio)
);
""")

conn.execute("""
CREATE TABLE permissao_andar(
    id_usuario INTEGER NOT NULL,
    id_predio INTEGER NOT NULL,
    id_andar INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio),
    FOREIGN KEY(id_andar) REFERENCES andar(id_andar)
);
""")

conn.execute("""
INSERT INTO usuario(nome)
	VALUES ("Karine"), ("Giovanna"), ("Gabriel"), ("Pedro"), ("Daniel"), ("Michele"), ("Isabela");
""")

conn.execute("""
INSERT INTO predio(capacidade_predio)
	VALUES (10), (10), (10), (10), (10), (10), (10)
""")

conn.execute("""
INSERT INTO andar(id_predio, capacidade_andar)
	VALUES (1,2), (1,3), (1,5), (2,2), (2,3), (2,5), (3,2), (3,6), (3,2), (4,4), (4, 2), (4,2), (4,2),
(5, 2), (5, 2), (5, 3), (5, 3), (6, 2), (6, 2), (6, 2), (6, 2), (6, 2), (7,2), (7,4), (7, 4)
""")
'''

conn.execute("""
INSERT INTO permissao_complexo(id_usuario, tipo_usuario)
	VALUES (1, 'Visitante'), (3, 'Funcionario'), (4, 'Visitante'), (2, 'Administrador'), (5, 'Funcionario'), (6, 'Visitante'), (7, 'Visitante')
""")

conn.execute("""
INSERT INTO permissao_predio(id_usuario, id_predio)
	VALUES (1, 2), (1,3), (1,5), (2,1), (2,2), (2,4), (2,6), (3,7), (3,5), (4,2), (4,6), (5,3), (5,7), (6,1), (6,6), (7,7)
""")

conn.execute("""
INSERT INTO permissao_andar(id_usuario, id_predio, id_andar)
	VALUES (1,1,1), (1,1,3), (2,1,1), (2,1,2), (2,1,3), (2,2,4), (2,2,5), (2,2,6), (3,5,15), (3,7,24)
""")

print("successfully operation")

conn.commit()
conn.close()
