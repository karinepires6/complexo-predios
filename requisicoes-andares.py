#Servidor que irá tratar as requisições de acesso
#referentes ao complexos

import time
import zmq
import sys
import credenciados as Credenciados

lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()      # lista provisória de credenciados no complexo

porta = "5555"                                          # Porta especificada para receber requisições referentes a andares
context = zmq.Context()
socket = context.socket(zmq.REP)                        # Socket usado para responder as requisições
socket.bind("tcp://*:"+ porta)                          

socket_requisicao = context.socket(zmq.REQ)             # Socket para fazer requisições para predios, se necessário
socket.connect("tcp://localhost:5556")                  # Porta especificada para tratamento de requisições para prédios


while True:

    requisicao = socket.recv_string()                   # Recebe a mensagem do cliente
    id_andar, id_predio, id_complexo, id_usuario, grau_usuario = requisicao.split() # Tratamento dos dados da mensagem recebida

    print(id_andar, id_predio, id_complexo, id_usuario, grau_usuario)

    if grau_usuario == "Visitante":                     # Encaminhamento dependendo do Grau do cliente
        # Tratamento para visitantes
    elif grau_usuario == "Funcionario":
        # Tratamento para funcionarios
    elif grau_usuario == "Administrador":
        # Tratamento para administradores
    else:
        # Caso de erro no grau



    socket.send_string("Deu certo")
    time.sleep(1)
