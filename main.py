from Candidato import Candidato
from Partido import Partido
from Cargo import Cargo
from Voto import Voto

lista_partidos = []
lista_cargos = []
lista_candidatos = []
lista_votos_realizados = []

menu_principa = ''' 
1- Cria Partido\n
2- Cria Cargo\n
3- Cria Candidato\n
4- Cria Eleitor e Vota\n
6- Apuração\n
Escolha: '''

def criar_eleitor():
  Voto().set_eleitor(lista_cargos, lista_candidatos, lista_votos_realizados)
  

def criar_partido():
  nome = input("nome: ")
  sigla = input("sigla: ")
  numero = input("numero: ")
  partido = Partido(nome, sigla, numero)
  if partido not in lista_partidos:
    lista_partidos.append(partido)
  else:
    print("\n\n partido já existe \n\n")

def criar_cargo():
    nome = input("nome do cargo: ")
    qt_de_digitos = input("quantidade de digitos: ")
    cargo = Cargo(nome, qt_de_digitos)
    if cargo not in lista_cargos:
        lista_cargos.append(cargo)
    else:
        print("\n\n Cargo já existente! \n\n")

def criar_candidator():
  nome = input("nome: ")
  titulo = input("titulo de eleitor: ")
  qt_votos = 0
  candidato = Candidato(nome, titulo, qt_votos)
  if candidato.escolher_partido(lista_partidos) and candidato.escolher_cargo(lista_cargos):
    candidato.set_numero()
    if candidato not in lista_candidatos:
      lista_candidatos.append(candidato)

def apuracao():
  lista_ordenada = lista_votos_realizados.copy()
  lista_ordenada.sort(key=lambda x: x.qt_votos)
  lista_ordenada.reverse()
  inter = 0
  for inter in range(0, len(lista_ordenada)):
    print("{} Candidato: {} com {} votos".format(inter + 1, lista_ordenada[inter].nome, lista_ordenada[inter].qt_votos))
  if len(lista_ordenada) == 0:
    print("Ainda não houve votação")


def menu():
  while(True):
    try:
      escolha =int(input(menu_principa))
      if escolha == 1: criar_partido()
      if escolha == 2: criar_cargo()
      if escolha == 3: criar_candidator()
      if escolha == 4: criar_eleitor()
      if escolha == 6: apuracao()
      if escolha == 0: break
    except:
      print("Por favor escolha uma opção que esteja no menu!")

menu()