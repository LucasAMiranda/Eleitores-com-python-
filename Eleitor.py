from Pessoa import Pessoa

class Eleitor(Pessoa):
  def __init__(self, nome: str, titulo: str, votou: bool = False):
    Pessoa.__init__(self, nome, titulo)
    self.votou = votou