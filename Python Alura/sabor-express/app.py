import os

restaurantes = ['Dom & Arte', 'Tastee']

# Nome do programa
def exibir_nome_do_programa():
  print("""
  ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
  ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
  ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
  ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
  ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
# Opções do programa
def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Ativar restaurante')
  print('4. Sair\n')

def voltar_ao_menu_principal():
  input('Digite algo para voltar ao menu principal')
  main()
# Opcao invalida
def opcao_invalida():
  print('Opcao inválida\n')
  voltar_ao_menu_principal

# Escolher opções
def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opçao: '))

    if opcao_escolhida == 1:
      cadastrar_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      ativar_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()
    
# Cadastrar restaurante
def cadastrar_restaurante():
  os.system('cls')
  # Armazenar coleção de dados
  print('Cadastro de novo restaurante\n')
  nome_do_restaurante = input('Nome do restaurante: ')

  # Add na lista restaurantes
  restaurantes.append(nome_do_restaurante)

  print(f'O restaurante {nome_do_restaurante} foi cadastrado')
  voltar_ao_menu_principal()

# Listar restaurantes
def listar_restaurantes():
  os.system('cls')
  print('Listando os restaurantes\n')

  for restaurante in restaurantes:
    print(f'- {restaurante}')

  voltar_ao_menu_principal()

# Ativar restaurante
def ativar_restaurante():
  os.system('cls')
  
  voltar_ao_menu_principal()
# Finalizar app
def finalizar_app():
  finalizar_app()


# Função que controla o projeto
def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()