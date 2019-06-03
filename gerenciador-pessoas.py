#Servidor que irá tratar as requisições de acesso
#referentes aos andares

import time
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REP)
porta = "5559"
socket.bind("tcp://*:"+ porta)                          #Socket faz a conexão com o servidor

lista_andares = []          # elemento = [[id_local], população, [lista_users]]
lista_predios = []          # elemento = [[id_local], população, [lista_users]]
lista_complexos = []        # elemento = [[id_local], população, [lista_users]]

max_andar = 10              # população máxima nos andares
max_predio = 100            # população máxima nos prédios
max_complexo = 1000         # população máxima nos complexos



while True:
    print("Esperando requisição")
    requisicao = socket.recv_string()                   #Recebe a mensagem do cliente
    operacao, id_complexo, id_predio, id_andar, visitante = requisicao.split()       #Tratamento da mensagem

    if id_andar != None:
        #Adiciona ou remove do complexo, predio e andar
        if operacao == "ENTRADA":
            entrada = [id_complexo, id_predio, id_andar]    # Formata entrada
            for andar in lista_andares:                # Verifica se o andar existe
                if entrada not in andar:
                    print("Andar inexistente")
                else:                                   # O andar existe
                    if andar[1] == max_andar:
                        socket.send_string("CAPACIDADE ANDAR")
                    else:
                        andar[1] += 1
                        break
            entrada = [id_complexo, id_predio]
            for predio in lista_predios:                # Verifica se o andar existe
                if entrada not in predio:
                    print("Predio inexistente")
                else:                                   # O andar existe
                    if predio[1] == max_predio:
                        socket.send_string("CAPACIDADE ANDAR")
                    else:
                        predio[1] += 1
                        break
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    if complexo[1] == max_complexo:
                        socket.send_string("CAPACIDADE COMPLEXO")
                    else:
                        complexo[1] += 1
                        break
            socket.send_string("OK")
            #Adiciona
            
        elif operacao == "SAIDA":
            #remove
            entrada = [id_complexo, id_predio, id_andar]    # Formata entrada
            for andar in lista_andares:                # Verifica se o andar existe
                if entrada not in andar:
                    print("Andar inexistente")
                else:                                   # O andar existe
                    andar[1] -= 1                       # Decrementa a população do andar
                    break
            entrada = [id_complexo, id_predio]
            for predio in lista_predios:                # Verifica se o andar existe
                if entrada not in predio:
                    print("Predio inexistente")
                else:                                   # O andar existe
                    predio[1] -= 1                      # Decrementa a população do andar
                    break
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    complexo[1] -= 1
                    break
            socket.send_string("OK")
    elif id_predio != None:
        #Adiciona ou remove do complexo e no predio
        if operacao == "ENTRADA":
            #Adiciona
            entrada = [id_complexo, id_predio]
            for predio in lista_predios:                # Verifica se o andar existe
                if entrada not in predio:
                    print("Predio inexistente")
                else:                                   # O andar existe
                    if predio[1] == max_predio:
                        socket.send_string("CAPACIDADE PREDIO")
                    else:
                        predio[1] += 1                       # Incrementa a população do andar
                        break
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    if complexo[1] == max_complexo:
                        socket.send_string("CAPACIDADE COMPLEXO")
                    else:
                        complexo[1] += 1
                        break
            socket.send_string("OK")
        elif operacao == "SAIDA":
            #remove
            entrada = [id_complexo, id_predio]
            for predio in lista_predios:                # Verifica se o andar existe
                if entrada not in predio:
                    print("Predio inexistente")
                else:                                   # O andar existe
                    andar[1] -= 1                       # Incrementa a população do andar
                    break
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    complexo[1] -= 1
            socket.send_string("OK")
    elif id_complexo != None:
        #Adiciona ou remove do complexo
        if operacao == "ENTRADA":
            #Adiciona
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    if complexo[1] == max_complexo:
                        socket.send_string("CAPACIDADE COMPLEXO")
                    else:
                        complexo[1] += 1
                        break
            socket.send_string("OK")
        elif operacao == "SAIDA":
            #remove
            entrada = [id_complexo]
            for complexo in lista_complexos:
                if entrada not in complexo:
                    print("Complexo inexistente")
                else:
                    complexo[1] -= 1
            socket.send_string("OK")


