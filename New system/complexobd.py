# connect_db.py
# 01_create_db.py
import sqlite3

#Criando Schema 'complexo'
conn = sqlite3.connect('complexo.db')

print("Opened database successfully")

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
    tipo_usuario INTEGER NOT NULL,
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

conn.commit()
conn.close()