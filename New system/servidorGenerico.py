import zmq
import time
import sys 


usuario_permitidos_predios = ["1", "2"]
usuario_permitidos_andar = ["1", "2"]
predios_disponiveis = ["1", "2"]
andares_disponiveis = ["1", "2"]

'''
topicfilter = "1001"
context = zmq.Context()
socketReceberRequisicao = context.socket(zmq.SUB)
portaGerenciador = "5558"
socketReceberRequisicao.connect("tcp://localhost:"+portaGerenciador)
socketReceberRequisicao.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

mensagem = socketReceberRequisicao.recv()
topico, dadomensagem = mensagem.split()
print(dadomensagem)
'''

#realiza a autenticacao e liberacao do acesso ao predio ou andar
def Autentica(id_user, id_predio, id_andar, cargo):
    if id_predio == None and id_andar == None:
        return "Não há solicitacao de acesso para predio e nem andar"
    elif id_predio != None and id_andar == None:
        if id_predio in predios_disponiveis:
            if id_user in usuario_permitidos_predios:
                return "Acesso liberado no predio %s" % id_predio
            else:
                return "%s não autorizado a acessar o predio %s" % (cargo, id_predio)
        else:
            return "O predio nao existe"
    elif id_predio != None and id_andar != None:
        if id_predio in predios_disponiveis:
            if id_andar in predios_disponiveis:
                if id_user in usuario_permitidos_andar:
                    return "Acesso liberado no predio %s, andar %s" % (id_predio, id_andar)
                else:
                    return "Usuario %s nao possui permissao para acessar o predio %s no andar %s" % (id_user, id_predio, id_andar)
            else:
                return "o Andar não existe"
        else:
            return "O predio nao existe"
    else:
        return "Acesso Invalido"


context = zmq.Context()
porta_servidor = "5559"
socketReceberRequisicao = context.socket(zmq.REP)
socketReceberRequisicao.bind("tcp://*:"+ porta_servidor) 

mensagem_Chegada = socketReceberRequisicao.recv()

mensagem_Chegada = mensagem_Chegada.decode()
id_user, id_predio, id_andar, cargo =  mensagem_Chegada.split()

print(f"%s %s %s %s" % (id_user, id_predio, id_andar, cargo))
print(mensagem_Chegada)
mensagem_Saida = Autentica(id_user, id_predio, id_andar, cargo)

socketReceberRequisicao.send_string("%s" % mensagem_Saida)


valor = id_predio in predios_disponiveis
print(valor)
