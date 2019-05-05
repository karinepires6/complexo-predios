import pessoa as Pessoa
import predio as Predio
import andar as Andar

##
# ID das Pessoas credenciadas: 2, 5, 7
# ID dos Prédios: 1, 2
# ID dos Andares: 1, 2, 3, 4, 5
##

##
# Especificação dos acessos:
# Pessoa 2 tem acesso ao prédio 1 e aos andares 2, 4
# Pessoa 5 tem acesso ao prédio 2 e aos andares 3, 5
# Pessoa 7 tem acesso ao prédio 1 e aos andares 1, 4 e 5 e ao prédio 2 com acesso ao andar 3
##
class Credenciados:
    
    def retornaListaCredenciados():


        lista_credenciados = []                     #lista provisória de credenciados no complexo
        lista_credenciados.append(Pessoa.Pessoa("2", [Predio.Predio("1", [Andar.Andar("2"), Andar.Andar("4")])]))
        lista_credenciados.append(Pessoa.Pessoa("5", [Predio.Predio("2", [Andar.Andar("3"), Andar.Andar("5")])]))
        lista_credenciados.append(Pessoa.Pessoa("7", [Predio.Predio("1", [Andar.Andar("1"), Andar.Andar("4"), Andar.Andar("5")]), Predio.Predio("2", [Andar.Andar("3")])]))

        return lista_credenciados
