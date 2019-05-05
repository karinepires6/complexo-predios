#Servidor que irá tratar as requisições de acesso
#referentes aos andares

import time
import zmq
import sys


porta = sys.argv[1]                                     #Recebe a porta como argumento na hora da execução do código

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta)                          #Socket faz a conexão com o servidor

lista_credenciados = ("2", "5", "7")                    #lista provisória de credenciados no andar

while True:
    print("Esperando requisição")
    requisicao = socket.recv_string()                   #Recebe a mensagem do cliente
    id_requisicao, visitante = requisicao.split()       #Tratamento da mensagem

    print("CLIENTE: %s" %id_requisicao)                 #informação da requisição será exibida do andar
    print("CREDENCIAL: %s" % visitante)

    if (id_requisicao in lista_credenciados) and (visitante == "cadastrado"):       #Tratamento das requisições
        socket.send_string("Cliente %s permitido e credenciado" % id_requisicao)    #caso de cliente na lista do andar e credenciado
    else:
        if visitante == "visitante":                                                #caso de cliente visitando o andar
            socket.send_string("Cliente %s permitido como visitante"% id_requisicao)
        else:                                                                       #caso o cliente informe que é credenciado e não consta na lista
            socket.send_string("Cliente nao permitido!")

    time.sleep(1)
