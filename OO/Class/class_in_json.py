"""
Exercício - Salve sua class em JSON
Salve os dados da sua classe em JSON
Crie novamente as instâncias da calsse com os dados salvos
Faça em arquivos separados
"""
# Arquivo onde está o json
CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Pessoa('Maria', 33)
p2 = Pessoa('Joana', 21)
p3 = Pessoa('Joana', 11)

bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
  json.dump(bd, arquivo, ensure_ascii=False, indent=2)