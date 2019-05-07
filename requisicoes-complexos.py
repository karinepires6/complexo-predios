#Servidor que irá tratar as requisições de acesso
#referentes ao complexos

import time
import zmq
import sys
# import credenciados as Credenciados

# lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()      # lista provisória de credenciados no complexo

porta = "5557"                                          # Porta especificada para receber requisições referentes a predios
context = zmq.Context()
socket = context.socket(zmq.REP)                        # Socket usado para responder as requisições
socket.bind("tcp://*:"+ porta)                          


# O conteudo da mensagem que requsicoes_complexos vai receber é:
# requisicao = (id_complexo, id_usuario, grau_usuario)

# requisicoes_complexos não precisa enviar mensagem, já que é a camada mais abaixo

while True:
    requisicao = socket.recv_string()                   # Recebe a mensagem do cliente
    id_complexo, id_usuario, grau_usuario = requisicao.split() # Tratamento dos dados da mensagem recebida

    print(id_complexo, id_usuario, grau_usuario)

    if grau_usuario == "Visitante":                     # Encaminhamento dependendo do Grau do cliente
        print("REALIZA AUTENTICAÇÂO DO USUARIO VISITANTE NO PREDIO")
        # 
        # REALIZA AUTENTICAÇÂO DO USUÁRIO NO COMPLEXO
        # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
        #         
        socket.send_string("Permitido") 
        # Tratamento para visitantes
    elif grau_usuario == "Funcionario":
        print("REALIZA AUTENTICAÇÂO DO USUARIO FUNCIONARIO NO COMPLEXO")
        # 
        # REALIZA AUTENTICAÇÂO DO USUÁRIO NO COMPLEXO
        # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
        #         
        socket.send_string("Permitido") 
        # Tratamento para funcionarios
    elif grau_usuario == "Administrador":
        print("REALIZA AUTENTICAÇÂO DO USUARIO ADMINISTRADOR NO COMPLEXO")
        # 
        # REALIZA AUTENTICAÇÂO DO USUÁRIO NO COMPLEXO
        # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
        #         
        socket.send_string("Permitido") 
        # Tratamento para administradores
    else:
        print("NÃO É NENHUM DOS GRAUS")
        socket.send_string("Negado")
        # Caso de erro no grau


# FIM DO while True: