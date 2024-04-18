  # Collections -> Mais de um elemento / Vários elementos

# Exemplo: Idade de vários usuários
# idade1 = 39
# idade2 = 30
# idade3 = 27

# print(idade1)
# print(idade2)
# print(idade3)

idades = [39, 30, 27, 18]

tipo = type(idades) # -> List

# List funciona como um array, porém array e list são tipos diferentes

# Tamanho
len(idades) # -> 4 

# Acessando uma idade
# print(idades[3])

# Adicionar valores
# Adiciona no fim da lista
idades.append(15)
# print(idades)

# Passar por todos os elementos
# for idade in idades:
#   print(idade)

# Remover elemento
# Remove o primeiro
# idades.remove(30)
# print(idades)

# Remover tudo da lista
# idades.clear()
# print(idades)

# Adicionar mais elementos
# idades.insert(0, 20)
# print(idades)

idades.extend([27, 19])
# print(idades)

# idades_no_ano_que_vem = []
# for idade in idades:
#   idades_no_ano_que_vem.append(idade + 1)

# print(idades_no_ano_que_vem)

# idades_no_ano_que_vem = [(idade+1) for idade in idades]

# print(idades_no_ano_que_vem)

# idade_maior_21 = [(idade) for idade in idades if idade > 21]

# print(idade_maior_21)


# list comprehension
# def next_year(idade):
#   return idade+1

# idade_maior_21 = [next_year(idade) for idade in idades if idade > 21]

# print(idade_maior_21)


# MUTABILIDADE

def faz_processamento_de_visualizacao(lista):
  print(len(lista))

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)

idades