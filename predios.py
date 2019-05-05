#Servidor que irá tratar as requisições de acesso
#referentes aos predios

import time
import zmq
import sys
import credenciados as Credenciados

lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()
 
porta = sys.argv[1]                                     #Recebe a porta como argumento na hora da execução do código

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta)                          #Socket faz a conexão com o servidor

while True:
    print("Esperando requisição")
    requisicao = socket.recv_string()                   #Recebe a mensagem do cliente
    id_requisicao, id_predio_solicitado, visitante = requisicao.split()       #Tratamento da mensagem

    print("CLIENTE: %s" %id_requisicao)                 #informação da requisição será exibida no servidor
    print("CREDENCIAL: %s" % visitante)

    flagAutorizadoNoPredio = False
    for credenciado in lista_credenciados:
        if(credenciado.id == id_requisicao):
            for predio in credenciado.listaPredios:
                if(predio.id == id_predio_solicitado):
                    flagAutorizadoNoPredio = True
                    break
            if(flagAutorizadoNoPredio):
                break

    if (flagAutorizadoNoPredio):       #Tratamento das requisições
        socket.send_string("Cliente %s permitido no prédio solicitado" % id_requisicao)    #caso de cliente na lista do predio e credenciado
    else:
        socket.send_string("Cliente nao permitido!")

    time.sleep(1)
