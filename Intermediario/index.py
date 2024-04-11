"""
  -> Functions  -> def nameFunction():
  -> Parametros -> Argumentos -> def Print(a ,b , c): 

  def imprimir(a, b, c):
  print('Argumento: ', a)
  print('Argumento: ', b)
  print('Argumento: ', c)


imprimir(10, 20, 30)
"""


"""
  -> Argumentos nomeados e não nomeados
  -> Argumentos nomeados tem nome com sinal de igual
  -> Argumentos não nomeado recebe apenas o argumento (valor)

  def soma(x, y, z):
  print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2)
soma(1, y=2, z=5)

soma(1, 2, 3, sep='-')
"""

"""
Valores padrão para paramentros
Ao definir uma função, os parametros podem ter valores padrão.
Caso o valor não seja enviado para o paramentro, o valor padrão será usado

def soma(x, y, z=None):
  if z is not None:
    print(f'Z nao eh None: {x=} y={y} {z=}', '|', x + y + z)
  else:
    print(f'{x=} y={y} {z=}', '|', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
"""

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Escopo Global -> Escopo onde o código é alcançavel
Escopo local -> Escopo onde apenas nomes do mesmo local podem ser alcançados
# Escopo global
y = 20 

def escopo():
  # Escopo local
  x = 1
  print(x, y)

escopo()

x = 1

def escopo():
  global x
  x = 10

  def outra_funcao():
    global x 
    x = 11
    y = 2
    print(x, y)

  outra_funcao()
  print(x)

print(x)
escopo()


def soma(x, y):
  return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1 + soma2)
"""


"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

# DESEMPACOTAMENTO

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
  total = 0
  for numero in args:
    total = total + numero
  print(total)

soma(1, 2, 3, 4, 5, 6)
"""


# def multiplica(*args):
#   total = 1

#   for num in args:
#     total *= num

#   return total

# print(multiplica(1, 2, 3, 4, 5, 6))



# Higher Order Functions 
# Funções de primeira classe


"""
Exercício
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parametro

def duplica(num):
  return num * 2

def triplica(num):
  return num * 3

def quadriplica(num):
  return num * 4


func_duplica = duplica(10)
func_triplica = triplica(10)
func_quadriplica = quadriplica(10)

print(func_duplica, func_triplica, func_quadriplica)
"""

"""
Métodos úteis
"""


# Sets - Conjuntos em Python (tipo set)
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# s3 = s1 | s2
# s4 = s1 & s2
# s5 = s1 - s2
# s6 = s1 ^ s2


# print(s3)
# print(s4)
# print(s5)
# print(s6)


