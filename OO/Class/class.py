"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus própros atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações
Por conveção, usamos PascalCase para nomes de classes
Classe -> Molde (Geralmente em dados)
Instancia da class (objeto ) -> Tem dados
Uma class pode gravar várias instâncias
Na classe o self é a própria instância
"""

class Pessoa:
  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome

p1 = Pessoa('Helter', 'Xavier')


print(p1.nome)
print(p1.sobrenome)
