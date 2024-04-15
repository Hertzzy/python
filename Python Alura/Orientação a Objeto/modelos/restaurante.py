# O QUE É UMA CLASSE?
# Abstração do mundo real
# Qualquer restaurante que for criar deve ter esses atributos:
#         nome, categoria, ativo

# Criar uma classe
# Criar um novo restaurante
class Restaurante:
  nome = ''
  categoria = ''
  ativo = False

# Estancia um resturante
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

# Estancia um resturante
restaurante_pizza = Restaurante()
restaurante_praca.nome = 'Tastee'
restaurante_praca.categoria = 'Lanche'


# Restaurantes dentro de uma LISTA
restaurantes = [restaurante_praca, restaurante_pizza]

#DIR
print(vars(restaurante_praca))