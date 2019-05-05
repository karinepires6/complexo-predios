#Servidor que irá tratar as requisições de acesso
#referentes ao complexos

import time
import zmq
import sys

import pessoa as Pessoa
import predio as Predio
import andar as Andar

##
# ID das Pessoas credenciadas: 2, 5, 7
# ID dos Prédios: 1, 2
# ID dos Andares: 1, 2, 3, 4, 5
##

##
# Especificação dos acessos:
# Pessoa 2 tem acesso ao prédio 1 e aos andares 2, 4
# Pessoa 5 tem acesso ao prédio 2 e aos andares 3, 5
# Pessoa 7 tem acesso ao prédio 1 e aos andares 1, 4 e 5 e ao prédio 2 com acesso ao andar 3
##

lista_credenciados = []                                 #lista provisória de credenciados no complexo

lista_credenciados.append(Pessoa.Pessoa("2", [Predio.Predio("1", [Andar.Andar("2"), Andar.Andar("4")])]))
lista_credenciados.append(Pessoa.Pessoa("5", [Predio.Predio("2", [Andar.Andar("3"), Andar.Andar("5")])]))
lista_credenciados.append(Pessoa.Pessoa("7", [Predio.Predio("1", [Andar.Andar("1"), Andar.Andar("4"), Andar.Andar("5")]), Predio.Predio("2", [Andar.Andar("3")])]))

porta = "5000"                                     #Recebe a porta como argumento na hora da execução do código

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta)                          #Socket faz a conexão com o servidor

while True:
    print("Esperando requisição")
    requisicao = socket.recv_string()                   #Recebe a mensagem do cliente
    id_requisicao, visitante = requisicao.split()       #Tratamento da mensagem

    print("CLIENTE: %s" %id_requisicao)                 #informação da requisição será exibida do servidor
    print("CREDENCIAL: %s" % visitante)

    flagCredenciado = False
    for credenciado in lista_credenciados:
        if(credenciado.id == id_requisicao):
            flagCredenciado = True
            break;

    if (flagCredenciado) and (visitante == "cadastrado"):       #Tratamento das requisições
        socket.send_string("Cliente %s permitido e credenciado" % id_requisicao)    #caso de cliente na lista do complexo e credenciado
    else:
        if visitante == "visitante":                                                #caso de cliente visitando o complexo
            socket.send_string("Cliente %s permitido como visitante"% id_requisicao)
        else:                                                                       #caso o cliente informe que é credenciado e não consta na lista
            socket.send_string("Cliente nao permitido!")

    time.sleep(1)
