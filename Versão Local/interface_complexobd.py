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

