import zmq
import time
import sys 

porta_gerenciador = "5556"
context = zmq.Context()
socket_Catraca = context.socket(zmq.REQ)
socket_Catraca.connect("tcp://localhost:" + porta_gerenciador)

socket_Catraca.send_string("%s %s %s %s %s" % ("ENTRADA", "1", None, None, "VISITANTE"))

mensagem_Recebida = socket_Catraca.recv()
mensagem_Recebida = mensagem_Recebida.decode()
print(mensagem_Recebida)

