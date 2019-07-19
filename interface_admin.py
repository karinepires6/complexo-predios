import zmq
import zerorpc
import sys


porta_interfaceBD = "5563"
socketInterfaceBD = zerorpc.Client()
socketInterfaceBD.connect("tcp://ec2-3-219-203-114.compute-1.amazonaws.com:"+ porta_interfaceBD)

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
            print("Para inserir um novo usuario pressione 1 \n")
            print("Para inserir um novo predio pressione 2 \n")
            print("Para inserir um novo andar em um predio existente pressione 3 \n")
            print("Para dar permissao de acesso ao complexo a um usuario pressione 4 \n")
            print("Para dar permissao de acesso de um usuario a um predio pressione 5 \n")
            print("Para dar permissao de acesso de um usuario a um andar pressione 6 \n")
            opcaoInsercao = int(input("Digite sua opcao: \n"))
            
            if opcaoInsercao == 1:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    nome_usuario = str(input("Digite o nome do novo usuario: \n"))
                    socketInterfaceBD.inserirUsuario(id_usuario, nome_usuario)       
                except sqlite3.Error:
                    print("Essa identificacao de usuario ja existe \n")
            
            if opcaoInsercao == 2:
                try:
                    id_predio = int(input("Digite a identificacao do predio: \n"))
                    capacidade_predio = int(input("Digite a capacidade do predio: \n"))
                    socketInterfaceBD.inserirPredio(id_predio, capacidade_predio)
                except sqlite3.Error:
                    print("Essa identificacao de predio ja existe \n")
            
            if opcaoInsercao == 3:
                try:
                    id_andar = int(input("Digite a identificacao do novo andar: \n"))
                    capacidade_andar = int(input("Digite a capacidade do novo andar: \n"))
                    id_predio = int(input("Digite a identificacao de um predio existente: \n"))
                    socketInterfaceBD.inserirAndar(id_andar, id_predio, capacidade_andar)
                except sqlite3.Error:
                    print("O predio informado nao existe \n")
            
            if opcaoInsercao == 4:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    tipo_usuario = str(input("Digite o tipo de usuario (Visitante ou Funcionario): \n"))
                    socketInterfaceBD.habilitarPermissaoComplexo(id_usuario, tipo_usuario)
                except sqlite3.errror:
                    print("O usuario informado nao existe \n")
            
            if opcaoInsercao == 5:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    socketInterfaceBD.habilitarPermissaoPredio(id_usuario, id_predio)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
    
            if opcaoInsercao == 6:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    socketInterfaceBD.habilitarPermissaoAndar(id_usuario, id_predio, id_andar)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
                    
        elif opcao == 3:
            print("Para remover um  usuario pressione 1 \n")
            print("Para remover um  predio pressione 2 \n")
            print("Para remover um  andar em um predio existente pressione 3 \n")
            print("Para retirar a  permissao de acesso ao complexo de um usuario pressione 4 \n")
            print("Para retirar a  permissao de acesso de um usuario de um predio pressione 5 \n")
            print("Para retirar a permissao de acesso de um usuario de um andar pressione 6 \n")
            opcaoRemocao = int(input("Digite sua opcao: \n"))
            
            if opcaoRemocao == 1:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    nome_usuario = str(input("Digite o nome do  usuario: \n"))
                    socketInterfaceBD.removerUsuario(id_usuario, nome_usuario)       
                except sqlite3.Error:
                    print("Essa identificacao de usuario nao existe  \n")
            
            if opcaoRemocao == 2:
                try:
                    id_predio = int(input("Digite a identificacao do predio: \n"))
                    capacidade_predio = int(input("Digite a capacidade do predio: \n"))
                    socketInterfaceBD.removerPredio(id_predio, capacidade_predio)
                except sqlite3.Error:
                    print("Essa identificacao de predio não existe \n")
            
            if opcaoRemocao == 3:
                try:
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    capacidade_andar = int(input("Digite a capacidade do  andar: \n"))
                    id_predio = int(input("Digite a identificacao de um predio existente: \n"))
                    socketInterfaceBD.removerAndar(id_andar, id_predio, capacidade_andar)
                except sqlite3.Error:
                    print("O andar informado nao existe \n")
            
            if opcaoRemocao == 4:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    tipo_usuario = str(input("Digite o tipo de usuario (Visitante ou Funcionario): \n"))
                    socketInterfaceBD.desabilitarPermissaoComplexo(id_usuario, tipo_usuario)
                except sqlite3.errror:
                    print("O usuario informado nao existe \n")
            
            if opcaoRemocao == 5:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    socketInterfaceBD.desabilitarPermissaoPredio(id_usuario, id_predio)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
    
            if opcaoRemocao == 6:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    socketInterfaceBD.desabilitarPermissaoAndar(id_usuario, id_predio, id_andar)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")


        else:
            sys.exit()

if __name__ == "__main__":

    main()
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
            print("Para inserir um novo usuario pressione 1 \n")
            print("Para inserir um novo predio pressione 2 \n")
            print("Para inserir um novo andar em um predio existente pressione 3 \n")
            print("Para dar permissao de acesso ao complexo a um usuario pressione 4 \n")
            print("Para dar permissao de acesso de um usuario a um predio pressione 5 \n")
            print("Para dar permissao de acesso de um usuario a um andar pressione 6 \n")
            opcaoInsercao = int(input("Digite sua opcao: \n"))
            
            if opcaoInsercao == 1:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    nome_usuario = str(input("Digite o nome do novo usuario: \n"))
                    socketInterfaceBD.inserirUsuario(id_usuario, nome_usuario)       
                except sqlite3.Error:
                    print("Essa identificacao de usuario ja existe \n")
            
            if opcaoInsercao == 2:
                try:
                    id_predio = int(input("Digite a identificacao do predio: \n"))
                    capacidade_predio = int(input("Digite a capacidade do predio: \n"))
                    socketInterfaceBD.inserirPredio(id_predio, capacidade_predio)
                except sqlite3.Error:
                    print("Essa identificacao de predio ja existe \n")
            
            if opcaoInsercao == 3:
                try:
                    id_andar = int(input("Digite a identificacao do novo andar: \n"))
                    capacidade_andar = int(input("Digite a capacidade do novo andar: \n"))
                    id_predio = int(input("Digite a identificacao de um predio existente: \n"))
                    socketInterfaceBD.inserirAndar(id_andar, id_predio, capacidade_andar)
                except sqlite3.Error:
                    print("O predio informado nao existe \n")
            
            if opcaoInsercao == 4:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    tipo_usuario = str(input("Digite o tipo de usuario (Visitante ou Funcionario): \n"))
                    socketInterfaceBD.habilitarPermissaoComplexo(id_usuario, tipo_usuario)
                except sqlite3.errror:
                    print("O usuario informado nao existe \n")
            
            if opcaoInsercao == 5:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    socketInterfaceBD.habilitarPermissaoPredio(id_usuario, id_predio)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
    
            if opcaoInsercao == 6:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    socketInterfaceBD.habilitarPermissaoAndar(id_usuario, id_predio, id_andar)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
                    
        elif opcao == 3:
            print("Para remover um  usuario pressione 1 \n")
            print("Para remover um  predio pressione 2 \n")
            print("Para remover um  andar em um predio existente pressione 3 \n")
            print("Para retirar a  permissao de acesso ao complexo de um usuario pressione 4 \n")
            print("Para retirar a  permissao de acesso de um usuario de um predio pressione 5 \n")
            print("Para retirar a permissao de acesso de um usuario de um andar pressione 6 \n")
            opcaoRemocao = int(input("Digite sua opcao: \n"))
            
            if opcaoRemocao == 1:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    nome_usuario = str(input("Digite o nome do  usuario: \n"))
                    socketInterfaceBD.removerUsuario(id_usuario, nome_usuario)       
                except sqlite3.Error:
                    print("Essa identificacao de usuario nao existe  \n")
            
            if opcaoRemocao == 2:
                try:
                    id_predio = int(input("Digite a identificacao do predio: \n"))
                    capacidade_predio = int(input("Digite a capacidade do predio: \n"))
                    socketInterfaceBD.removerPredio(id_predio, capacidade_predio)
                except sqlite3.Error:
                    print("Essa identificacao de predio não existe \n")
            
            if opcaoRemocao == 3:
                try:
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    capacidade_andar = int(input("Digite a capacidade do  andar: \n"))
                    id_predio = int(input("Digite a identificacao de um predio existente: \n"))
                    socketInterfaceBD.removerAndar(id_andar, id_predio, capacidade_andar)
                except sqlite3.Error:
                    print("O andar informado nao existe \n")
            
            if opcaoRemocao == 4:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    tipo_usuario = str(input("Digite o tipo de usuario (Visitante ou Funcionario): \n"))
                    socketInterfaceBD.desabilitarPermissaoComplexo(id_usuario, tipo_usuario)
                except sqlite3.errror:
                    print("O usuario informado nao existe \n")
            
            if opcaoRemocao == 5:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    socketInterfaceBD.desabilitarPermissaoPredio(id_usuario, id_predio)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")
    
            if opcaoRemocao == 6:
                try:
                    id_usuario = int(input("Digite a identificacao do usuario: \n"))
                    id_predio  = int(input("Digite a identificacao do predio: \n"))
                    id_andar = int(input("Digite a identificacao do andar: \n"))
                    socketInterfaceBD.desabilitarPermissaoAndar(id_usuario, id_predio, id_andar)
                except sqlite3.error:
                    print("Alguma das informacoes nao existe \n")


        else:
            sys.exit()

if __name__ == "__main__":

    main()
