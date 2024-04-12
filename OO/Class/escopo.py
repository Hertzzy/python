"""
Escopo da classe e de métodos da classe
"""
class Animal:
  # nome = 'Leao'

  def __init__(self, nome):
    self.nome = nome

    variavel = 'valor'
    print(variavel)

leao = Animal(nome='Leao')
print(leao.nome)