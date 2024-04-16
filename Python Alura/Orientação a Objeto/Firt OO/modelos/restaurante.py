from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
# O QUE É UMA CLASSE?
# Abstração do mundo real
# Qualquer restaurante que for criar deve ter esses atributos:
#         nome, categoria, ativo
# É UM MODELO PARA CRIAR OBJETOS

# Criar uma classe
# Criar um novo restaurante
class Restaurante:
  # Todos restaurante que é criado vai para a lista restaurantes
  restaurantes = []
  # Método INIT -> Contructor -> Quando criar uma instancia o método init é chamdo
  # self -> Referencia da instancia usada
  # CONSTRUCTOR
  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    # ativo é um atributo privado
    self._ativo = False

    self._avaliacao = []
    self._cardapio = []
    # Adicionando restaurante à LIST restaurante
    Restaurante.restaurantes.append(self)

  # Retorna os atributos como STRING
  def __str__(self):
    return f'{self.nome} | {self.categoria}'

  @classmethod
  def listar_restaurantes(cls):
    print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')

    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avalicoes).ljust(25)} | {restaurante.ativo}')
  
  # Decorator -> Modificar como o atributo vai ser lido
  @property
  def ativo(self):
    return '✅' if self._ativo else '❌'

  # Método alterar estado
  def alterar_estado(self):
    self._ativo = not self._ativo

  # Método de avaliação
  def receber_avaliacao(self, cliente, nota):
    if 0 < nota < 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)

  # Método de média
  @property
  def media_avalicoes(self):
    if not self._avaliacao:
      return '-'
    
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)

    quantidade_de_notas = len(self._avaliacao)
    media = round(soma_das_notas / quantidade_de_notas, 1)
    return media

  
  def add_no_cardapio(self, item):
    # Verifica se o item está dentro do cardápio
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)
  
  @property
  def exibir_cardapio(self):
    print(f'Cardapio do restaurante {self._nome}\n')

    for i, item in enumerate(self._cardapio, start=1):
      # SE TIVER O ATRIBUTO
      # Se o atributo for descrição -> É UM PRATO
      # SE NÃO -> É UMA BEBIDA
      if hasattr(item, 'descricao'):
        mensagem_prato = f'{i}. Nome: {item} | Preco: R${item._preco} | Descricao: {item.descricao}'
        print(mensagem_prato)
      else:
        mensagem_bebida = f'{i}. Nome: {item} | Preco: R${item._preco} | Tamanho: {item.tamanho}'
        print(mensagem_bebida)

      
