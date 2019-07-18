import sqlite3
import zmq
import zerorpc

conn = sqlite3.connect('complexo.db')
cursor = conn.cursor()

class InterfaceBd(object):
	

	'''
	Retorna uma lista de usuários cadastrados no banco
	'''
	def listaUsuarios(self):
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
	def listaPredios(self):
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
	def listaAndaresPorPredio(self):
		cursor.execute("""
		SELECT * FROM andar
		""")

		listaAndares = []
		for andar in cursor.fetchall():
			listaAndares.append({"id_andar": andar[0], "id_predio": andar[1], "capacidade_andar": andar[2]})

		return listaAndares

	def listaUsuariosPermitidosComplexo(self):
		cursor.execute("""
		SELECT * FROM permissao_complexo
		""")

		lista = []
		for permissao in cursor.fetchall():
			lista.append({"id_usuario": permissao[0], "tipo_usuario": permissao[1]})

		return lista


	def listaUsuariosPermitidosNosPredios(self):
		cursor.execute("""
		SELECT * from permissao_predio	
		""")

		lista = []
		for permissao in cursor.fetchall():
			lista.append({"id_usuario": permissao[0], "id_predio": permissao[1]})

		return lista


	def listaUsuariosPermitidosPorAndar(self):
		cursor.execute("""
		SELECT * from permissao_andar	
		""")

		lista = []
		for permissao in cursor.fetchall():
			lista.append({"id_usuario": permissao[0], "id_predio": permissao[1], "id_andar": permissao[2]})

		return lista
	
	def inserirUsuario(self, id_usuario, nome_usuario):
		lista = [(id_usuario, nome_usuario)]
		cursor.executemany("""INSERT INTO usuario (id_usuario, nome) VALUES (?, ?)""", lista)
		conn.commit()

	def inserirPredio(self, id_predio, capacidade_predio):
		lista = [(id_predio, capacidade_predio)]
		cursor.executemany("""INSERT INTO predio (id_predio, capacidade_predio) VALUES (?, ?)""", lista)
		conn.commit()

	def inserirAndar(self, id_andar, id_predio, capacidade_andar):
		lista = [(id_andar, id_predio, capacidade_andar)]
		cursor.executemany("""INSERT INTO andar (id_andar, id_predio, capacidade_andar) VALUES (?, ?)""", lista)
		conn.commit()
	
	def habilitarPermissaoComplexo(self, id_usuario, tipo_usuario):
		lista = [(id_usuario, tipo_usuario)]
		cursor.executemany("""INSERT INTO permissao_complexo (id_usuario, tipo_usuario) VALUES (?, ?)""", lista)
		conn.commit()

	def habilitarPermissaoPredio(self, id_usuario, id_predio):
		lista = [(id_usuario, id_predio)]
		cursor.executemany("""INSERT INTO permissao_predio (id_usuario, id_predio) VALUES (?, ?)""", lista)
		conn.commit()

	def habilitarPermissaoAndar(self, id_usuario, id_predio, id_andar):
		lista = [(id_usuario, id_predio, id_andar)]
		cursor.executemany("""INSERT INTO permissao_andar (id_usuario, id_predio, id_andar) VALUES (?, ?, ?)""", lista)
		conn.commit()
	 	
	
	def removerUsuario(self, id_usuario, nome_usuario):
		lista = [(id_usuario, nome_usuario)]
		cursor.executemany("""DELETE FROM usuario WHERE id_usuario = ? AND nome = ?""", lista)
		conn.commit()

	def removerPredio(self, id_predio, capacidade_predio):
		lista = [(id_predio, capacidade_predio)]
		cursor.executemany("""DELETE FROM predio WHERE id_predio = ? AND capacidade_predio = ?""", lista)
		conn.commit()

	def removerAndar(self, id_andar, id_predio, capacidade_andar):
		lista = [(id_andar, id_predio, capacidade_andar)]
		cursor.executemany("""DELETE FROM andar WHERE id_andar = ? AND id_predio= ? AND capacidade_andar = ?""", lista)
		conn.commit()
	
	def desabilitarPermissaoComplexo(self, id_usuario, tipo_usuario):
		lista = [(id_usuario, tipo_usuario)]
		cursor.executemany("""DELETE FROM  permissao_complexo WHERE id_usuario = ? AND tipo_usuario = ?""", lista)
		conn.commit()

	def desabilitarPermissaoPredio(self, id_usuario, id_predio):
		lista = [(id_usuario, id_predio)]
		cursor.executemany("""DELETE FROM permissao_predio WHERE id_usuario = ? AND id_predio = ?""", lista)
		conn.commit()

	def desabilitarPermissaoAndar(self, id_usuario, id_predio, id_andar):
		lista = [(id_usuario, id_predio, id_andar)]
		cursor.executemany("""DELETE FROM  permissao_andar WHERE id_usuario = ? AND id_predio = ? AND id_andar = ?""", lista)
		conn.commit()


	def fecharConexao(self):
		conn.close()


socketRpc = zerorpc.Server(InterfaceBd())
portaInterfaceBD = "5563"
socketRpc.bind("tcp://*:"+portaInterfaceBD)
socketRpc.run()

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

