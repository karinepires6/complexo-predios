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

	return cursor.fetchall();


'''
Retorna uma lista dos prédios cadastrados no banco
'''
def listaPredios():
	cursor.execute("""
	SELECT * FROM predio;
	""")
	return cursor.fetchall();


'''
Retorna a lista de andares por prédios
'''
def listaAndaresPorPredio():
	cursor.execute("""
	SELECT * FROM andar
	""")
	return cursor.fetchall()

def listaUsuariosPermitidosComplexo():
	cursor.execute("""
	SELECT * FROM permissao_complexo
	""")
	return cursor.fetchall()


def listaUsuariosPermitidosNosPredios():
	cursor.execute("""
	SELECT * from permissao_predio	
	""")
	return cursor.fetchall()


def listaUsuariosPermitidosPorAndar():
	cursor.execute("""
	SELECT * from permissao_andar	
	""")
	return cursor.fetchall()

"""
def main():
	lista = listaAndaresPorPredio()
	print('Andares por predio')
	for item in lista:
		print(item)


	lisUsuarios = listaUsuariosPermitidosPorAndar()
	print('Lista Usuarios Permitidos por andar')
	for usuario in lisUsuarios:
		print(usuario)


if __name__ == "__main__":
    main()
"""
conn.close()

