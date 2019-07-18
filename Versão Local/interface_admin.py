import zmq
import zerorpc
import sys


porta_interfaceBD = "5563"
socketInterfaceBD = zerorpc.Client()
socketInterfaceBD.connect("tcp://localhost:"+ porta_interfaceBD)

'''
O administrador pode visualizar e alterar  todas as informações do complexo

'''
def main():

    while True:
        print("Você esta na interface de administrador \n")
        print("Para visualizar as informações do complexo pressione 1 \n")
        print("Para inserir alguma informação do complexo pressione 2 \n")
        print("Para remover alguma informação do complexo pressione 3 \n")
        print("Para sair pressione qualquer tecla diferente das anteriores \n")
        opcao = int(input("Digite sua opcao: \n"))

        if opcao == 1:
            print("Visualizar usuários cadastrados pressione 1 \n")
            print("Visualizar a quantidade de predios do complexo pressione 2 \n")
            print("Visualizar a lista de andares por prédio pressione 3 \n")
            print("Visualizar a lista de usuarios permitidos no complexo pressione 4 \n")
            print("Visualizar a lista de usuarios permitidos por predio pressione 5 \n")
            print("Visualizar a lista de usuarios permitidos por andar pressione 6 \n")
            opcaoVisualizacao = int(input("Digite sua opcao: \n"))

            if opcaoVisualizacao == 1:
                usuariosCadastrados = socketInterfaceBD.listaUsuarios()
                for lista in usuariosCadastrados:
                    print("id_usuario: " + str(lista["id_usuario"]) + "\n")
                    print("nome: " +  str(lista["nome"]) + "\n")

            if opcaoVisualizacao == 2:            
                prediosCadastrados = socketInterfaceBD.listaPredios()
                for lista in prediosCadastrados:
                    print("id_predio: " + str(lista["id_predio"]) + "\n")
                    print("capacidade_predio: " +  str(lista["capacidade_predio"]) + "\n")
            
            if opcaoVisualizacao == 3:            
                andaresPredios = socketInterfaceBD.listaAndaresPorPredio()
                for lista in andaresPredios:
                    print("id_andar:" +  str(lista["id_andar"]) + "\n")
                    print("id_predio: " + str(lista["id_predio"]) + "\n")
                    print("capacidade_andar: " +  str(lista["capacidade_andar"]) + "\n")
            
            if opcaoVisualizacao == 4:
                usuariosPermitidosComplexo = socketInterfaceBD.listaUsuariosPermitidosComplexo()
                for lista in usuariosPermitidosComplexo:
                    print("id_usuario: " + str(lista["id_usuario"]) + "\n")
                    print("tipo_usuario: " + str(lista["tipo_usuario"]) + "\n")
            
            if opcaoVisualizacao == 5:
                usuariosPermitidosPredio = socketInterfaceBD.listaUsuariosPermitidosNosPredios()
                for lista in usuariosPermitidosPredio:
                    print("id_usuario: " + str(lista["id_usuario"]) + "\n")
                    print("id_predio: " + str(lista["id_predio"]) + "\n")
                   
            if opcaoVisualizacao == 6:
                usuariosPermitidosAndar = socketInterfaceBD.listaUsuariosPermitidosPorAndar()
                for lista in usuariosPermitidosAndar:
                    print("id_usuario: " + str(lista["id_usuario"]) + "\n")
                    print("id_predio: " + str(lista["id_predio"]) + "\n")
                    print("id_andar:" +  str(lista["id_andar"]) + "\n")
            

        elif opcao == 2:
            socketInterfaceBD.inserirUsuario("4", "Teste")

        
        else:
            sys.exit()

if __name__ == "__main__":

    main()
