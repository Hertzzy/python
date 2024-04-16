from  modelos.restaurante import Restaurante

# restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_mexicana = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_japones.receber_avaliacao('Guilherme', 10)
restaurante_japones.receber_avaliacao('Lais', 8)

# restaurante_japones.alterar_estado()

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()