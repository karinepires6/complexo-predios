import sqlite3

#Criando Schema 'complexo'
conn = sqlite3.connect('complexo.db')
cursor = conn.cursor()

print("Opened database successfully")

conn.execute("""
CREATE TABLE IF NOT EXISTS usuario(
    id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS predio(
    id_predio INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    capacidade_predio INTEGER NOT NULL
);
""")


conn.execute("""
CREATE TABLE IF NOT EXISTS andar(
    id_andar INTEGER NOT NULL,
    id_predio INTEGER NOT NULL,
    capacidade_andar INTEGER NOT NULL,
    PRIMARY KEY (id_andar, id_predio),
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio)
);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS permissao_complexo(
    id_usuario INTEGER NOT NULL,
    tipo_usuario VARCHAR(50) NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS permissao_predio(
    id_usuario INTEGER NOT NULL,
    id_predio INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio)
);
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS permissao_andar(
    id_usuario INTEGER NOT NULL,
    id_predio INTEGER NOT NULL,
    id_andar INTEGER NOT NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_predio) REFERENCES predio(id_predio),
    FOREIGN KEY(id_andar) REFERENCES andar(id_andar)
);
""")
'''
conn.execute("""
INSERT INTO usuario(id_usuario, nome)
	VALUES (1, "Giovanna"), (2, "Gabriel"), (3, "Karine")
""")

conn.execute("""
INSERT INTO predio(id_predio, capacidade_predio)
	VALUES (1, 10), (2, 10), (3,10)
""")

conn.execute("""
INSERT INTO andar(id_predio, id_andar, capacidade_andar)
	VALUES (1, 1, 3), (1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 2, 3), (2, 3, 4), (3, 1, 3), (3, 2, 3), (3, 3, 4)
""")


conn.execute("""
INSERT INTO permissao_complexo(id_usuario, tipo_usuario)
	VALUES (1, 'Visitante'), (2, 'Funcionario'), (3, 'Funcionario')
""")

conn.execute("""
INSERT INTO permissao_predio(id_usuario, id_predio)
	VALUES (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)
""")

conn.execute("""
INSERT INTO permissao_andar(id_usuario, id_predio, id_andar)
	VALUES (1,1,1), (1,1,3), (2,1,1), (2,1,2), (2,1,3), (2,2,3), (2,3,1), (2,3,2)
""")
'''


print("successfully operation")

conn.commit()
conn.close()
