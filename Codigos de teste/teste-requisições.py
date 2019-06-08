import zmq
import time
import sys 
import random



lista_requisicoes = [
    ("ENTRADA", "2", "1", "3", "Administrador"), 
    ("SAIDA", "2", "2", "2", "Funcionario"),
    ("ENTRADA", "2", "3", "5", "Visitante"),
    ("ENTRADA", "2", "4", "1", "Funcionario"),
    ("ENTRADA", "2", "2", "1", "Funcionario"),
    ("SAIDA", "2", "1", "4", "Funcionario"),
    ("ENTRADA", "2", "2", "2", "Administrador"),
    ("ENTRADA", "2", "3", "3", "Visitante"),
    ("SAIDA", "2", "5", "1", "Funcionario"),
    ("ENTRADA", "2", "3", "2", "Visitante"),
    ("SAIDA", "2", "2", "3", "Administrador"),
    ("ENTRADA", "2", "1", "6", "Visitante"),
]



porta_gerenciador = "5556"
context = zmq.Context()
socket_Catraca = context.socket(zmq.REQ)
socket_Catraca.connect("tcp://localhost:" + porta_gerenciador)



while True:
    socket_Catraca.send_string("%s %s %s %s %s" % (lista_requisicoes[random.randrange(len(lista_requisicoes))]))

    mensagem_Recebida = socket_Catraca.recv()
    mensagem_Recebida = mensagem_Recebida.decode()
    print(mensagem_Recebida)
    time.sleep(1)

