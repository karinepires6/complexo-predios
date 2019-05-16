#Cliente vai forjar Ids e fazer requisições de acesso
#para os servidores que vão trata-las.

import time
import zmq
import sys
from random import randrange



# Sumario de portas:
# Porta para andares: 5555
# Porta para predios: 5556
# Porta para complexos: 5557

context = zmq.Context()
# socket = context.socket(zmq.REQ)                  # Socket que faz a requisição com a localização desejada
# socket.connect("tcp://localhost:"+ porta)       # Socket faz a conexão com o servidor

socket_andar = context.socket(zmq.REQ)
socket_predio = context.socket(zmq.REQ)
socket_complexo = context.socket(zmq.REQ)
socket_andar.connect("tcp://localhost:5555")
socket_predio.connect("tcp://localhost:5556")
socket_complexo.connect("tcp://localhost:5557")

# As requsições do cliente vão de andar para complexo
# As requsições do cliente serão na forma de lstas onde:
# requsição = (Complexo_desejado , Predio_desejado , Andar_Desejado , id_usuário, Grau_Usuario)


def gerador_Requisicao():                         #Função que gera requisições de entrada

    requisicao_entrada = [None, None, None, None, None]
    
    profundidade = randrange(1, 4)                # Gerador da profundidade de acesso do usuário da requisição
                                                  # Ex: profundidade 3 = Complexo->Predio->Andar
                                                  # Ex: profundidade 2 = Complexo->Predio
    for count in range(profundidade):
        requisicao_entrada[count] = randrange(1, 11)    # Geração dos IDs do locais alvos de visitação


    id_usuario = randrange(1, 21)                 # Gera a ID do usuário
    requisicao_entrada[3] = id_usuario            # A ID do usuário fica na posição [3] da lista requisição

   
    grau_usuario = randrange(1,4)                #Gera o grau de visita do usuário que fica na posição [4] da lista de requisição    
    if grau_usuario == 1:                        # 1 - Visitante
        requisicao_entrada[4] = "Visitante"
    elif grau_usuario == 2:
        requisicao_entrada[4] = "Funcionario"    # 2 - Funcionario
    elif grau_usuario == 3:
        requisicao_entrada[4] = "Administrador"  # 3 - Administrador
    return requisicao_entrada
# FIM DE gerador_Requisicao()



while True:

    requisicao_entrada = gerador_Requisicao()           # Recebe uma requisição de usuário
    print(requisicao_entrada)

    if requisicao_entrada[2] != None:                   # Existe requisição para andar
        # socket.connect("tcp://localhost:5555")          # Escolhe a porta para andar
        socket_andar.send_string("%i %i %i %i %s" % (requisicao_entrada[0], requisicao_entrada[1], requisicao_entrada[2], requisicao_entrada[3], requisicao_entrada[4]))
        print("Enviado para ANDAR")
        #requisita entrada no andar
        resposta = socket_andar.recv_string()
        if resposta == "Permitido":
            print("Usuario %i permitido com acesso de %s" %(requisicao_entrada[3], requisicao_entrada[4]))
        elif resposta == "Populacao":
            print("Usuario %i negado. O andar já atingiu a população máxima")
        else:
            print("Requisicao negada, usuário %i nao tem permissao." % requisicao_entrada[3])

        time.sleep(1)
    elif requisicao_entrada[1] != None:                 # Existe requisição para predio, mas não para andar
        # socket.connect("tcp://localhost:5556")          # Escolhe a porta para predio
        socket_predio.send_string("%i %i %i %s" % (requisicao_entrada[0], requisicao_entrada[1], requisicao_entrada[3], requisicao_entrada[4]))
        print("Enviado para PREDIO")
        # requisita entrada no predio
        resposta = socket_predio.recv_string()
        if resposta == "Permitido":
            print("Usuario %i permitido com acesso de %s" %(requisicao_entrada[3], requisicao_entrada[4]))
        elif resposta == "Populacao":
            print("Usuario %i negado. O prédio já atingiu a população máxima")
        else:
            print("Requisicao negada, usuário %i nao tem permissao." % requisicao_entrada[3])

        time.sleep(1)
    elif requisicao_entrada[0] != None:                 # Existe requisição para complexo, mas não para predio e nem andar
        # socket.connect("tcp://localhost:5557")          # Escolhe a porta para andar
        socket_complexo.send_string("%i %i %s" % (requisicao_entrada[0], requisicao_entrada[3], requisicao_entrada[4]))
        print("Enviado para COMPLEXO")

        # requisita entrada no complexo
        resposta = socket_complexo.recv_string()
        if resposta == "Permitido":
            print("Usuario %i permitido com acesso de %s" %(requisicao_entrada[3], requisicao_entrada[4]))
        elif resposta == "Populacao":
            print("Usuario %i negado. O complexo já atingiu a população máxima")
        else:
            print("Requisicao negada, usuário %i nao tem permissao." % requisicao_entrada[3])

        time.sleep(1)
    else:
        time.sleep(1)
        print("NAO ENTRA EM NADA")
        continue


    # resposta recebe "Permitido" ou "Negado"

    # resposta = socket.recv_string()
    # if resposta == "Permitido":
    #     print("Usuario %i permitido com acesso de %s" %(requisicao_entrada[3], requisicao_entrada[4]))
    # else:
    #     print("Requisicao negada, usuário %i nao tem permissao.")

    # time.sleep(1)