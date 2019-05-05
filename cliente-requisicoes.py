#Cliente vai forjar Ids e fazer requisições de acesso
#para os servidores que vão trata-las.

import time
import zmq
import sys
from random import randrange


porta = "5000"                     #Recebe a porta como argumento na hora da execução do código

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:"+ porta) #Socket faz a conexão com o servidor

while True:

    id_cliente = randrange(1, 10)         #Randomiza IDs de credenciais.
    if randrange(1,10)%2 == 0:            #Cliente visitante?
        visitante = True    
    else:
        visitante = False


    if visitante:                                                           #Informa se o cliente é um visitante ou não
        print("Requisicao:\nCliente %i\nCredencial: Visitante" % id_cliente)
        socket.send_string("%i %s" % (id_cliente, "visitante"))             #envio da mensagem ao servidor
    else:
        print("Requisicao:\nCliente %i\nCredencial: Cadastrado" % id_cliente)
        socket.send_string("%i %s" % (id_cliente, "cadastrado"))            #envio da mensagem ao servidor

    






    resposta = socket.recv_string()                                         #Aguarda pela resposta do servidor
    print("Cliente %s %s " % (id_cliente, resposta))                        #Informa a resposta
    print("\n\n\n")
    time.sleep(1)