# LISTAS COM OBJETOS DE CLASSES

class ContaCorrente:
  def __init__(self, codigo, saldo):
    self.codigo = codigo
    self.saldo = 0
  
  def deposita(self, valor):
    self.saldo += valor
  
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
print(conta_do_gui)