#Servidor que irá tratar as requisições de acesso
#referentes ao predios

import time
import zmq
import sys
# import credenciados as Credenciados

# lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()      # lista provisória de credenciados no complexo

porta = "5556"                                          # Porta especificada para receber requisições referentes a predios
context = zmq.Context()
socket = context.socket(zmq.REP)                        # Socket usado para responder as requisições
socket.bind("tcp://*:"+ porta)                          

socket_requisicao = context.socket(zmq.REQ)             # Socket para fazer requisições para complexos, se necessário
socket_requisicao.connect("tcp://localhost:5557")                  # Porta especificada para tratamento de requisições para complexos


# O conteudo da mensagem que requsicoes_predios vai receber é:
# requisicao = (id_predio, id_complexo, id_usuario, grau_usuario)

while True:

    requisicao = socket.recv_string()                   # Recebe a mensagem do cliente
    id_predio, id_complexo, id_usuario, grau_usuario = requisicao.split() # Tratamento dos dados da mensagem recebida

    print(id_predio, id_complexo, id_usuario, grau_usuario)

    if grau_usuario == "Visitante":                     # Encaminhamento dependendo do Grau do cliente
        # Envia para requisicoes_complexos a id_complexo, id_andar, id_usuario e grau_usuario
        # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
        socket_requisicao.send_string("%s %s %s" % (id_complexo, id_usuario, grau_usuario))  
        resposta = socket_requisicao.recv_string()      
        if resposta == "Permitido":             
            print("REALIZA AUTENTICAÇÂO DO USUARIO VISITANTE NO PREDIO")
            # 
            # REALIZA AUTENTICAÇÂO DO USUÁRIO NO ANDAR
            # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
            #         
            socket.send_string("Permitido")        
        else:
            socket.send_string("Negado")
        # Tratamento para visitantes
    elif grau_usuario == "Funcionario":
        # Envia para requisicoes_complexos a id_complexo, id_andar, id_usuario e grau_usuario
        # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
        socket_requisicao.send_string("%s %s %s" % (id_complexo, id_usuario, grau_usuario))  
        resposta = socket_requisicao.recv_string()      
        if resposta == "Permitido":             
            print("REALIZA AUTENTICAÇÂO DO USUARIO VISITANTE NO PREDIO")
            # 
            # REALIZA AUTENTICAÇÂO DO USUÁRIO NO ANDAR
            # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
            #         
            socket.send_string("Permitido")        
        else:
            socket.send_string("Negado")
        # Tratamento para funcionarios
    elif grau_usuario == "Administrador":
        # Envia para requisicoes_complexos a id_complexo, id_andar, id_usuario e grau_usuario
        # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
        socket_requisicao.send_string("%s %s %s" % (id_complexo, id_usuario, grau_usuario))  
        resposta = socket_requisicao.recv_string()      
        if resposta == "Permitido":             
            print("REALIZA AUTENTICAÇÂO DO USUARIO VISITANTE NO PREDIO")
            # 
            # REALIZA AUTENTICAÇÂO DO USUÁRIO NO ANDAR
            # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
            #         
            socket.send_string("Permitido")        
        else:
            socket.send_string("Negado")
        # Tratamento para administradores
    else:
        print("NÃO É NENHUM DOS GRAUS")
        socket.send_string("Negado")
        # Caso de erro no grau

# FIM DO while True: