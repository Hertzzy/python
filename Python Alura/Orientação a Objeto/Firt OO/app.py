from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# CRIAR RESTAURANTE
restaurante_praca = Restaurante('Praca', 'Gourmet')
# CRIAR BEBIDA
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
# Aplicar desconto
bebida_suco.aplicar_desconto()
# CRIAR PRATO
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

# ADIONANDO ITEMS NO CARDAPIO
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)

def main():
  restaurante_praca.exibir_cardapio

if __name__ == '__main__':
  main()