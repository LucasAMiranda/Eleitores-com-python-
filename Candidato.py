from operator import truediv
from xmlrpc.client import Boolean
from Cargo import Cargo
from Pessoa import Pessoa

class Candidato(Pessoa):
    def __init__(self, nome, tit_eleitor, qt_votos):
        Pessoa.__init__(self, nome, tit_eleitor)
        self.partido = None
        self.cargo = None
        self.numero = None
        self.qt_votos = qt_votos

    def __str__(self) -> str:
        return "Nome: {} - Cargo: {} - Numero: {}".format(self.nome, self.cargo, self.numero)
    

    def __repr__(self) -> str:
        return "Nome: {} - Cargo: {} - Numero: {}".format(self.nome, self.cargo, self.numero)
    
    def __eq__(self, other):
        if isinstance(other, Candidato):
            return self.numero == other.numero
        return False
    
    def __lt__(self, other):
        return self.qt_votos < other.qt_votos

    def escolher_cargo(self, lista_cargos: list) -> bool:
        if (len(lista_cargos) == 0):
            print("\n\n<--------------------------> nao existe um cargo em aberto, crie um! <-------------------------->\n\n")
            return False
        i = 0
        for i in range(0,len(lista_cargos)):
            print("{} <---> para o cargo: {}".format(i, lista_cargos[i].nome_cargo))
        try:
            escolha = int(input("digite a opção do cargo que escolheu: "))
            if lista_cargos[escolha] in lista_cargos:
                self.cargo = lista_cargos[escolha]
                return True
            return False
        except:
            print("escolha digitada não corresponde a um número")
            return False

    def escolher_partido(self, lista_partidos: list) -> bool:
        if (len(lista_partidos) == 0):
            print("\n\n<--------------------------> nao existe um partido em aberto, crie um! <-------------------------->\n\n")
            return False
        i = 0
        for i in range(0,len(lista_partidos)):
            print("{} <---> para o partido: {}".format(i, lista_partidos[i].nome))
        try:
            escolha = int(input("digite a opção do partido que escolheu: "))
            if lista_partidos[escolha] in lista_partidos:
                self.partido = lista_partidos[escolha]
                return True
            return False
        except:
            print("escolha digitada não corresponde a um número")
            return False

    def ler_numero(self) -> int:
        return self.numero

    def set_numero(self):
        numero = input("numero: ")
        if len(numero) ==  int(self.cargo.qt_de_digitos) and numero.isdigit():
            self.numero = str(numero)
        else:
            print("numero invalido")
            return self.set_numero()


