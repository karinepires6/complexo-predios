#Cliente vai forjar Ids e fazer requisições de acesso
#para os servidores que vão trata-las.

import time
import zmq
import sys
from random import randrange


porta = sys.argv[1]              #Recebe a porta como argumento na hora da execução do código

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:"+ porta) #Socket faz a conexão com o servidor

while True:

    id_cliente = randrange(1, 10)         #Randomiza IDs de credenciais.
    if randrange(1,10)%2 == 0:            #Cliente visitante?
        visitante = True    
    else:
        visitante = False


    if visitante:                         #Informa se o cliente é um visitante ou não
        socket.send_string("%i %i" % (id_cliente, "visitante"))         #envio da mensagem ao servidor
    else:
        socket.send_string("%i %i" % (id_cliente, "cadastrado"))        #envio da mensagem ao servidor

    






    resposta = socket.recv()                                        #Aguarda pela resposta do servidor
    print("Cliente %s %s " % (id_cliente, resposta))                #Informa a resposta

    time.sleep(1)