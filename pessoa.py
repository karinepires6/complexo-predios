import predio as Predio

class Pessoa(object):
    def __init__(self, id=None, listaPredios=Predio):
        self.id = id
        self.listaPredios = listaPredios