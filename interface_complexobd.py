import sqlite3

conn = sqlite3.connect('complexo.db')
cursor = conn.cursor()

'''
Retorna uma lista de usuários cadastrados no banco
'''
def listaUsuarios():
	cursor.execute("""
	SELECT * FROM usuario;
	""")

	lista = []
	for usuario in cursor.fetchall():
		lista.append({"id_usuario": usuario[0], "nome": usuario[1]})

	return lista

'''
Retorna uma lista dos prédios cadastrados no banco
'''
def listaPredios():
	cursor.execute("""
	SELECT * FROM predio;
	""")

	lista = []
	for predio in cursor.fetchall():
		lista.append({"id_predio": predio[0], "capacidade_predio": predio[1]})

	return lista

'''
Retorna a lista de andares por prédios
'''
def listaAndaresPorPredio():
	cursor.execute("""
	SELECT * FROM andar
	""")

	listaAndares = []
	for andar in cursor.fetchall():
		listaAndares.append({"id_andar": andar[0], "id_predio": andar[1], "capacidade_andar": andar[2]})

	return listaAndares

def listaUsuariosPermitidosComplexo():
	cursor.execute("""
	SELECT * FROM permissao_complexo
	""")

	lista = []
	for permissao in cursor.fetchall():
		lista.append({"id_usuario": permissao[0], "tipo_usuario": permissao[1]})

	return lista


def listaUsuariosPermitidosNosPredios():
	cursor.execute("""
	SELECT * from permissao_predio	
	""")

	lista = []
	for permissao in cursor.fetchall():
		lista.append({"id_usuario": permissao[0], "id_predio": permissao[1]})

	return lista


def listaUsuariosPermitidosPorAndar():
	cursor.execute("""
	SELECT * from permissao_andar	
	""")

	lista = []
	for permissao in cursor.fetchall():
		lista.append({"id_usuario": permissao[0], "id_predio": permissao[1], "id_andar": permissao[2]})

	return lista

def fecharConexao():
	conn.close()

"""
def main():
	lista = listaAndaresPorPredio()
	print('Andares por predio')
	for item in lista:
		print(item)
	
	fecharConexao()


if __name__ == "__main__":
    main()

"""

