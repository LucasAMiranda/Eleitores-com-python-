class Cargo:
    def __init__(self, nome: str, numero: str):
        self.nome_cargo = nome
        self.qt_de_digitos = numero

    def __eq__(self, other):
        if isinstance(other, Cargo):
            return self.nome_cargo == other.nome_cargo
        return False

    def __str__(self) -> str:
        return "Nome: {} - Quantidade de digitos: {}".format(self.nome_cargo, self.qt_de_digitos)
    def __repr__(self) -> str:
        return "Nome: {} - Quantidade de digitos: {}".format(self.nome_cargo, self.qt_de_digitos)