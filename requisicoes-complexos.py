#Servidor que irá tratar as requisições de acesso
#referentes ao complexos

import time
import zmq
import sys
import credenciados as Credenciados

lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()      # lista provisória de credenciados no complexo

porta = "5557"                                          # Porta especificada para receber requisições
context = zmq.Context()
socket = context.socket(zmq.REP)                        # Socket usado para responder as requisições
socket.bind("tcp://*:"+ porta)                          

socket_requisicao = context.socket(zmq.REQ)             # Socket para fazer requisições para predios, se necessário
socket.connect("tcp://localhost:5556")                  # Porta especificada para tratamento de requisições para prédios


while True:
   
    time.sleep(1)
