#Servidor que irá tratar as requisições de acesso
#referentes ao andares

import time
import zmq
import sys
# import credenciados as Credenciados

# lista_credenciados = Credenciados.Credenciados.retornaListaCredenciados()      # lista provisória de credenciados no complexo

porta = "5555"                                          # Porta especificada para receber requisições referentes a andares
context = zmq.Context()
socket = context.socket(zmq.REP)                        # Socket usado para responder as requisições
socket_requisicao = context.socket(zmq.REQ)             # Socket para fazer requisições para predios, se necessário
socket.bind("tcp://*:"+ porta)                          # Porta especificada para recever requisições
socket_requisicao.connect("tcp://localhost:5556")                  # Porta especificada para tratamento de requisições para prédios


POPULACAO_MAXIMA = 90                                   # População máxima aceita por andar.
populacao_atual = 0                                     # População atual do andar
n_andares = 10

lista_andares = []



def Criar_Andares():
    # A lista de andares é constituida por (Id_Andar, População_Andar)
    for a in range(n_andares):
        lista_andares.append((a+1, 0))
    

Criar_Andares()


def Verifica_Andar(id_andar):
    a = 1   #linha aleatória
    # Essa função verifica se um andar existe no prédio solicitado




# O conteudo da mensagem que requsicoes_andares vai receber é:
# requisicao = (id_andar, id_predio, id_complexo, id_usuario, grau_usuario)

while True:

    requisicao = socket.recv_string()                   # Recebe a mensagem do cliente
    id_andar, id_predio, id_complexo, id_usuario, grau_usuario = requisicao.split() # Tratamento dos dados da mensagem recebida

    print(id_andar, id_predio, id_complexo, id_usuario, grau_usuario)

    if lista_andares[id_andar][1] <= POPULACAO_MAXIMA:

        if grau_usuario == "Visitante":                     # Encaminhamento dependendo do Grau do cliente
            # Envia para requisicoes_predios a id_complexo, id_predio, id_usuario e grau_usuario
            # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
            socket_requisicao.send_string("%s %s %s %s" % (id_predio, id_complexo, id_usuario, grau_usuario))  
            resposta = socket_requisicao.recv_string()      
            if resposta == "Permitido":             
                # 
                # REALIZA AUTENTICAÇÂO DO USUÁRIO NO ANDAR
                # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
                #         
                socket.send_string("Permitido")        
            else:
                socket.send_string("Negado")
            # Tratamento para visitantes
        elif grau_usuario == "Funcionario":
            # Envia para requisicoes_predios a id_complexo, id_predio, id_usuario e grau_usuario
            # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
            socket_requisicao.send_string("%s %s %s %s" % (id_predio, id_complexo, id_usuario, grau_usuario))  
            resposta = socket_requisicao.recv_string()      
            if resposta == "Permitido":             
                # 
                # REALIZA AUTENTICAÇÂO DO USUÁRIO NO ANDAR
                # E SE FOR PERMITIDO, CONFIRMA A PERMISSÃO PARA O USUARIO
                #         
                socket.send_string("Permitido")        
            else:
                socket.send_string("Negado")
            # Tratamento para funcionarios
        elif grau_usuario == "Administrador":
            # Envia para requisicoes_predios a id_complexo, id_predio, id_usuario e grau_usuario
            # Esses dados serão tratados e uma resposta de que o usuário foi aceito ou não no predio virá
            socket_requisicao.send_string("%s %s %s %s" % (id_predio, id_complexo, id_usuario, grau_usuario))  
            resposta = socket_requisicao.recv_string()      
            if resposta == "Permitido":             
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
    
    else:
        socket.send_string("População")             # Mensagem de que o andar já atingiu a população limite.

# FIM DO while True: