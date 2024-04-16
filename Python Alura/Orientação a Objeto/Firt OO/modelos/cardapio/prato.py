from modelos.cardapio.item_cardapio import ItemCardapio

# A classe Prato vai herdar métodos e atributos de uma outra classe 
class Prato(ItemCardapio):
  def __init__(self, nome, preco, descricao):
    # Herda o inicializador
    # super -> Permite acessar informações de outra classe
    # Herda o nome e o preço
    # Descrição é específico da classe Prato
    super().__init__(nome, preco)
    self.descricao = descricao

  # Visualizar uma Bebida
  def __str__(self):
    return self._nome

  def aplicar_desconto(self):
    self._preco -= (self._preco * 0.05)
