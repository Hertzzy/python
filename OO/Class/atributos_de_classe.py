# Atributos de classe
class Pessoa:
  year = 2024

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_birthday_year(self):
    return Pessoa.year - self.age

p1 = Pessoa('Helter', 25)
p2 = Pessoa('Helena', 12)

print(p1.get_birthday_year())
print(p2.get_birthday_year())
