import zmq
import time
import sys 
import os
import string

porta_gerenciador = "5556"
context = zmq.Context()
socket_Catraca = context.socket(zmq.REQ)
socket_Catraca.connect("tcp://localhost:" + porta_gerenciador)

local = 1
# 0 = Sair do programa
# 1 = Portaria de complexo
# 2 = Dentro de complexo
# 3 = Dentro de predio
# 4 = Dentro de Andar
# 404 = Erro na autenticação


predio_destino = 0
andar_destino = 0




while local != 0:    
    if local == 1:
        # os.system("clear")
        print("Voce esta na portaria do complexo")
        print("Opcoes:\n1 - Informar destino."+
            "\n0 - Sair da aplicacao.")
        opcao = int(input("Digite sua opcao: "))
        if opcao == 1:
            opcao = int(input("Onde deseja ir:\n1 - Complexo.\n" +
                "2 - Predio.\n3 - Andar.\n0 - Voltar.\nDigite seua opcao:"))
            if opcao == 1:
                identificacao = input("\nDigite sua identificacao:")
                cargo = input("Digite seu cargo: ")
                cargo = cargo.title()
                socket_Catraca.send_string("%s %s %s %s %s" % ("ENTRADA", identificacao, "None", "None", "VISITANTE"))
                mensagem_Recebida = socket_Catraca.recv()
                mensagem_Recebida = mensagem_Recebida.decode()
                print(mensagem_Recebida)
                if mensagem_Recebida == "Não há solicitacao de acesso para predio e nem andar":
                    local = 2
                else:
                    local = 404
                
            if opcao == 2:
                identificacao = input("\nDigite sua identificacao: ")
                predio_destino = input("\nDigite a id do predio: ")
                cargo = input("Digite seu cargo: ")
                cargo = cargo.title()
                socket_Catraca.send_string("%s %s %s %s %s" % ("ENTRADA", identificacao, predio_destino, "None", "VISITANTE"))
                mensagem_Recebida = socket_Catraca.recv()
                mensagem_Recebida = mensagem_Recebida.decode()
                print(mensagem_Recebida)
                if mensagem_Recebida.find("Acesso liberado") != -1:
                    local = 3
                else:
                    local = 404
            if opcao == 3:
                identificacao = input("\nDigite sua identificacao: ")
                predio_destino = input("\nDigite a id do predio: ")
                andar_destino = input("\nDigite a id do andar: ")
                cargo = input("Digite seu cargo: ")
                cargo = cargo.title()
                socket_Catraca.send_string("%s %s %s %s %s" % ("ENTRADA", identificacao, predio_destino, andar_destino, "VISITANTE"))
                mensagem_Recebida = socket_Catraca.recv()
                mensagem_Recebida = mensagem_Recebida.decode()
                print(mensagem_Recebida)
                print(mensagem_Recebida.find("Acesso liberado"))
                if mensagem_Recebida.find("Acesso liberado") != -1:
                    local = 4
                else:
                    local = 404
            if opcao == 0:
                local = 0
    if local == 2:
        os.system("clear")
        print("Voce esta dentro do complexo")
        print("Opcoes:\n1 - Sair")
        opcao = int(input("Digite sua opcao: "))
        if opcao == 1:
            socket_Catraca.send_string("%s %s %s %s %s" % ("SAIDA", "1", "1", "1", "VISITANTE"))
            mensagem_Recebida = socket_Catraca.recv()
            mensagem_Recebida = mensagem_Recebida.decode()
            print(mensagem_Recebida)
            local = 1

    if local == 3:
        os.system("clear")
        print("Voce esta dentro do predio %s." % predio_destino)
        print("Opcoes:\n1 - Sair")
        opcao = int(input("Digite sua opcao: "))
        if opcao == 1:
            socket_Catraca.send_string("%s %s %s %s %s" % ("SAIDA", "1", predio_destino, "1", "VISITANTE"))
            mensagem_Recebida = socket_Catraca.recv()
            mensagem_Recebida = mensagem_Recebida.decode()
            print(mensagem_Recebida)
            local = 1
            
    if local == 4:
        os.system("clear")
        print("Voce esta dentro do predio %s, andar %s." % (predio_destino, andar_destino))
        print("Opcoes:\n1 - Sair")
        opcao = int(input("Digite sua opcao: "))
        if opcao == 1:
            socket_Catraca.send_string("%s %s %s %s %s" % ("SAIDA", "1", predio_destino, andar_destino, "VISITANTE"))
            mensagem_Recebida = socket_Catraca.recv()
            mensagem_Recebida = mensagem_Recebida.decode()
            print(mensagem_Recebida)
            local = 1

    if local == 404:
        os.system("clear")
        print("Ocorreu um erro, tente novamente.")
        time.sleep(3)
        local = 1
    elif local == 0:
        sys.exit()







# socket_Catraca.send_string("%s %s %s %s %s" % ("ENTRADA", "1", "1", "1", "VISITANTE"))

# mensagem_Recebida = socket_Catraca.recv()
# mensagem_Recebida = mensagem_Recebida.decode()
# print(mensagem_Recebida)

