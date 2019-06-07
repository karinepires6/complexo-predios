# -*- coding: utf-8 -*-
# O código do gerenciador vai ser responsável por gerenciar quem tem acesso ao complexo.
# Também irá gerenciar a quantidade de pessoas que estão presentes, tanto no complexo quanto
# nos prédios e andares.


import time
import zmq
import sys
import interface_complexobd as ComplexoService

# Sessão de definição de sockets:
# Socket que irá receber as requisições de entrada dos clientes
porta_servidor = "5555"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:"+ porta_servidor) 


porta_servidor_Generico = "5559"
socket_Generico = context.socket(zmq.REQ)
socket_Generico.connect("tcp://localhost:"+porta_servidor_Generico)


# Fim da definição de sockets

# Definição das listas de controle de usuários:
usuarios_permitidos_complexo = ComplexoService.listaUsuariosPermitidosComplexo()
usuarios_permitidos_predio = ComplexoService.listaUsuariosPermitidosNosPredios()
usuarios_permitidos_andar = ComplexoService.listaUsuariosPermitidosPorAndar()
# Fim da definição das listas


# Listas de locais
lista_predios = ComplexoService.listaPredios()
lista_andares = ComplexoService.listaAndaresPorPredio()


# Lista com quantidades presentes nos locais
# A quantidade de pessoas no complexo é apenas um inteiro
quantidade_complexo = 0
quantidade_predio = []
quantidade_andar = []
# Fim das listas


# Ininicializa as listas com as ids dos locais e zera a população de cada
def Inicializa_Listas(quantidade_predio, quantidade_andar):
    for predio in lista_predios:
        quantidade_predio.append((predio['id_predio'], 0))

    for andar in lista_andares:
        quantidade_andar.append((andar['id_predio'], andar['id_andar'], 0))

    


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
    mensagem = mensagem_recebida.split()
    if len(mensagem) == 10: # "Não há solicitacao de acesso para predio e nem andar"
        return mensagem_recebida
        
    elif len(mensagem) == 5: # "Acesso liberado no predio %s" % id_predio
        id_predio = int(mensagem[len(mensagem)-1])
        for predio in quantidade_predio:    # procura pelo predio no controle de populacao de predios
            if predio[0] == id_predio:
                predio[1] += 1          # aumenta a população do prédio em 1
                quantidade_complexo += 1 # aumenta a populacao do complexo
                break
        return mensagem_recebida

    elif len(mensagem) == 8: #  "%s não autorizado a acessar o predio %s" % (cargo, id_predio)
        return mensagem_recebida

    elif len(mensagem) == 4: # "O predio nao existe" ou "O andar nao existe"
        return mensagem_recebida

    elif len(mensagem) == 7: # "Acesso liberado no predio %s, andar %s" % (id_predio, id_andar)
        id_andar = int(mensagem[len(mensagem)-1])
        id_predio = int(mensagem[4])
        for andar in quantidade_andar:
            if andar[0] == id_predio and andar[1] == id_andar:
                andar[2] += 1
                for predio in quantidade_predio:
                    if predio[0] == id_predio:
                        predio[1] += 1
                        break
                quantidade_complexo += 1
                break

    elif len(mensagem) == 13: # "Usuario %s nao possui permissao para acessar o predio %s no andar %s" % (id_user, id_predio, id_andar)
        return mensagem_recebida

    elif len(mensagem) == 2:
        return mensagem_recebida




def Requisicao_Entrada(id_user, id_predio, id_andar, cargo):
    socket_Generico.send_string("%s %s %s %s" % (id_user, id_predio, id_andar, cargo))

    mensagem_Retorno = socket_Generico.recv_string()

    mensagem_tratada = Trata_mensagem_retorno(mensagem_Retorno)
    print(mensagem_tratada)

    return mensagem_tratada


def Requisicao_Saida(id_predio, id_andar):
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


def main():

    Inicializa_Listas(lista_predios, lista_andares)

    while True:
        #As requisições recebidas serão do tipo: [id_user, predio, andar, cargo]
        requisicao = socket.recv_string()
        requisicao = requisicao.decode()
        operacao, id_user, id_predio, id_andar, cargo = requisicao.split()

        if operacao == "ENTRADA":
            Requisicao_Entrada(id_user, id_predio, id_andar, cargo)
            
        elif operacao == "SAIDA":
            Requisicao_Saida(id_predio, id_andar)

        else:
            print("Operacao nao valida")




if __name__ == "__main__":
    ##main()
    #MensagemTeste()
    requisicao = socket.recv()
    requisicao = requisicao.decode()
    operacao, id_user, id_predio, id_andar, cargo = requisicao.split()
    resposta = Requisicao_Entrada(id_user, id_predio, id_andar, cargo)
    socket.send_string("%s" % (resposta))
    ComplexoService.fecharConexao()