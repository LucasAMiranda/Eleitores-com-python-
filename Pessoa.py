class Pessoa:
    def __init__(self, nome, tit_eleitor):
        self.nome = nome
        self.tit_eleitor = tit_eleitor

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return self.tit_eleitor == other.tit_eleitor
        return False

    def __str__(self) -> str:
        return "Nome: {}".format(self.nome)
        
    def __repr__(self) -> str:
        return "Nome: {}".format(self.nome)