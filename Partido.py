class Partido:
    def __init__(self, nome: str, sigla: str, numero: str):
        self.nome = nome
        self.sigla = sigla
        self.numero = numero

    def __eq__(self, other):
        if isinstance(other, Partido):
            nome = self.nome == other.nome
            sigla = self.sigla == other.sigla
            return sigla and nome
        return False

    def __str__(self) -> str:
        return "Nome: {} - Sigla: {} - Numero: {}".format(self.nome, self.sigla, self.numero)

    def __repr__(self) -> str:
        return "Nome: {} - Sigla: {} - Numero: {}".format(self.nome, self.sigla, self.numero)