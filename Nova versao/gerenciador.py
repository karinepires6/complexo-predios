# -*- coding: utf-8 -*-
# O código do gerenciador vai ser responsável por gerenciar quem tem acesso ao complexo.
# Também irá gerenciar a quantidade de pessoas que estão presentes, tanto no complexo quanto
# nos prédios e andares.


import time
import zmq
import zerorpc
import sys
#import interface_complexobd as ComplexoService
from ast import literal_eval

# Sessão de definição de sockets:
# Socket que irá receber as requisições de entrada dos clientes
porta_servidor = "5556"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta_servidor) 


porta_servidor_Generico = "5559"
socket_Generico = context.socket(zmq.REQ)
socket_Generico.connect("tcp://localhost:"+porta_servidor_Generico)

socketInterfaceBD = zerorpc.Client()
portaInterfaceBD = "5563"
socketInterfaceBD.connect("tcp://localhost:"+portaInterfaceBD)

# Fim da definição de sockets

# Definição das listas de controle de usuários:
usuarios_permitidos_complexo = socketInterfaceBD.listaUsuariosPermitidosComplexo()
usuarios_permitidos_predio = socketInterfaceBD.listaUsuariosPermitidosNosPredios()
usuarios_permitidos_andar = socketInterfaceBD.listaUsuariosPermitidosPorAndar()
# Fim da definição das listas


# Listas de locais
lista_predios = list(socketInterfaceBD.listaPredios())
lista_andares = list(socketInterfaceBD.listaAndaresPorPredio())





'''
# Definição das listas de controle de usuários:
usuarios_permitidos_complexo = ComplexoService.listaUsuariosPermitidosComplexo()
usuarios_permitidos_predio = ComplexoService.listaUsuariosPermitidosNosPredios()
usuarios_permitidos_andar = ComplexoService.listaUsuariosPermitidosPorAndar()
# Fim da definição das listas


# Listas de locais
lista_predios = list(ComplexoService.listaPredios())
lista_andares = list(ComplexoService.listaAndaresPorPredio())

'''
# Lista com quantidades presentes nos locais
# A quantidade de pessoas no complexo é apenas um inteiro
quantidade_complexo = 0
quantidade_predio = []
quantidade_andar = []
# Fim das listas


# Ininicializa as listas com as ids dos locais e zera a população de cada
def Inicializa_Listas(quantidade_predio, quantidade_andar):
    for predio in lista_predios:
        quantidade_predio.append([predio['id_predio'], 0])

    for andar in lista_andares:
        quantidade_andar.append([andar['id_predio'], andar['id_andar'], 0])

    


# Realiza a autenticação do usuário no complexo
def Autentica_Pessoa(id_user, cargo):
    # Se o usuário tem credencial de visitante, ele tem acesso
    if cargo == "VISITANTE":
        return True
    elif id_user in usuarios_permitidos_complexo: # Se não, apenas se for credenciado
        return True
    else:
        return False


def Trata_mensagem_retorno(mensagem_recebida):
    global quantidade_complexo
    mensagem_recebida = literal_eval(mensagem_recebida)
    if int(mensagem_recebida.get("tipoErro")) == 1: # "Não há solicitacao de acesso para predio e nem andar"
        return mensagem_recebida.get("mensagem")
    elif int(mensagem_recebida.get("tipoErro")) == 2: # "Acesso liberado no predio %s"
        id_predio = int(mensagem_recebida.get("id_predio"))
        for predio in quantidade_predio:    # procura pelo predio no controle de populacao de predios
            if predio[0] == id_predio:
                predio[1] += 1          # aumenta a população do prédio em 1
                quantidade_complexo += 1 # aumenta a populacao do complexo
                break
        return mensagem_recebida.get("mensagem")
    elif int(mensagem_recebida.get("tipoErro")) == 3: #  "%s não autorizado a acessar o predio %s" % (cargo, id_predio)
        return mensagem_recebida.get("mensagem")
    elif int(mensagem_recebida.get("tipoErro")) == 4 or int(mensagem_recebida.get("tipoErro")) == 7:
        return mensagem_recebida.get("mensagem")
    elif int(mensagem_recebida.get("tipoErro")) == 5: # "Acesso liberado no predio %s, andar %s" % (id_predio, id_andar)
        id_andar = int(mensagem_recebida.get("id_andar"))
        id_predio = int(mensagem_recebida.get("id_predio"))
        for andar in quantidade_andar:
            if andar[0] == id_predio and andar[1] == id_andar:
                andar[2] += 1
                for predio in quantidade_predio:
                    if predio[0] == id_predio:
                        predio[1] += 1
                        break
                quantidade_complexo += 1
                break
        return mensagem_recebida.get("mensagem")

    elif int(mensagem_recebida.get("tipoErro")) == 6: # "Usuario %s nao possui permissao para acessar o predio %s no andar %s" % (id_user, id_predio, id_andar)
        return mensagem_recebida.get("mensagem")
    else:
        return mensagem_recebida.get("mensagem") # Acesso Invalido



def Requisicao_Entrada(id_user, id_predio, id_andar, cargo):
    socket_Generico.send_string("%s %s %s %s" % (id_user, id_predio, id_andar, cargo))

    mensagem_Retorno = socket_Generico.recv_string()

    mensagem_tratada = Trata_mensagem_retorno(mensagem_Retorno)
    print(mensagem_tratada)

    return mensagem_tratada


def Requisicao_Saida(id_predio, id_andar):
    global quantidade_complexo
    if id_andar == "None":
        identificador_predio = int(id_predio)
        for predio in quantidade_predio:
            if predio[0] == identificador_predio:
                predio[1] -= 1
                quantidade_complexo -= 1
                break
    else:
        identificador_predio = int(id_predio)
        identificador_andar = int(id_andar)
        for andar in quantidade_andar:
            if andar[0] == identificador_predio and andar[1] == identificador_andar:
                andar[2] -= 1
                for predio in quantidade_predio:
                    if predio[0] == identificador_predio:
                        predio[1] -= 1
                        break
                quantidade_complexo -= 1
                break
    return "saiu"

def main():

    Inicializa_Listas(quantidade_predio, quantidade_andar)

    while True:
        #As requisições recebidas serão do tipo: [id_user, predio, andar, cargo]
        requisicao = socket.recv()
        requisicao = requisicao.decode()
        operacao, id_user, id_predio, id_andar, cargo = requisicao.split()

        if operacao == "ENTRADA":
            resposta = Requisicao_Entrada(id_user, id_predio, id_andar, cargo)
            socket.send_string("%s" % (resposta))
            
        elif operacao == "SAIDA":
            resposta = Requisicao_Saida(id_predio, id_andar)
            socket.send_string("%s" % (resposta))

        else:
            print("Operacao nao valida")




if __name__ == "__main__":
    main()
    #MensagemTeste()
   
   
    # requisicao = socket.recv()
    # requisicao = requisicao.decode()
    # operacao, id_user, id_predio, id_andar, cargo = requisicao.split()
    # resposta = Requisicao_Entrada(id_user, id_predio, id_andar, cargo)
    # socket.send_string("%s" % (resposta))
    
    
    socketInterfaceBD.fecharConexao()