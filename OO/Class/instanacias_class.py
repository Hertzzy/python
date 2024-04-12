# Metodos em instâncias de classes Python
# Método é um a função que está dentro da classe e usa o primeiro
#parametro tem que ser selff

class Carro:
  def __init__(self, nome):
    self.nome = nome
  
  def acelerar(self):
    print(f'{self.nome} esta acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
