from Cargo import Cargo
from Eleitor import Eleitor

def valida_escolha(escolha: str):
    if escolha.isdigit():
        return escolha
    else:
        print("sua escolha não é um número!")
        nova_escolha = input("numero do seu candidato: ")
        valida_escolha(nova_escolha)

class Voto:
    def __init__(self):
        self.eleitor = None
        self.candidato = []

    def set_eleitor(self, lista_cargos: list, lista_candidatos: list, lista_votos_realizados: list):
        nome = input("Nome do eleitor: ")
        titulo = input("Numero do titulo de eleitor: ")
        self.eleitor = Eleitor(nome, titulo, False)
        i = 0
        for i in range(0,len(lista_cargos)):
            cargo = lista_cargos[i]
            ops = {}
            j = 0
            for j in range(0,len(lista_candidatos)):
                candidato = lista_candidatos[j]
                if cargo == candidato.cargo:
                    print("nome: {}, partido: {}, cargo: {}, numero: {}\n".format(candidato.nome, candidato.partido.nome, candidato.cargo.nome_cargo, candidato.numero))
                    ops[candidato.numero] = candidato
            if len(ops) != 0:
                escolha = valida_escolha(input("numero do seu candidato: "))
                if escolha in ops:
                    if ops[escolha] not in lista_votos_realizados:
                        lista_votos_realizados.append(ops[escolha])
                    ops[escolha].qt_votos += 1
                    self.candidato.append(ops[escolha])
                else:
                    print("voto nulo")
            self.eleitor.votou = True