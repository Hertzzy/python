# Exibir informações na tela
# print('Helter Barbosa Xavier') 

# Tipos de dados imútaveis e primitivos
# print('---Tipos de dados imútaveis e primitivos---')
# str -> string
# print('Helter Xavier')
# int -> Números inteiros negativos || positivos
# print('25')
# float -> Números com ponto flutuante negativos || positivos
# print(10.5)
# boolean -> Valores TRUE || FALSE
# print(True)

# Converter dados
# print(int('1') + 1)

# print('----------------------------------------------')

# Variáveis em Python
# print('---Variáveis em Python---')
# As variáveis são iniciadas com letra minuscula
# Pode conter numeros, uderline e CamelCase
# nome_variavel = 'Helter'
# nome_completo = 'Helter Xavier'
# idade = 25
# print(f'Seu nome é {nome_completo} e sua idade é de {idade} anos!')

#Exercício 1
# print('--Exercício 1--')

# nome = 'Helter'
# sobrenome = 'Barbosa Xavier'
# idade = 25
# ano_nascimento = 1998

#if idade >= 18:
# maior_de_idade = True

# maior_de_idade = idade >= 18

# altura_metros = 1.71

# print('Nome', nome)
# print('Sobrenome',sobrenome )
# print('Idade', idade)
# print('Ano de nascimento', ano_nascimento)
# print('É maior de idade ?', maior_de_idade)
# print('ALtura em metros',altura_metros )

# Operadores Aritmétricos
# print('----------------------------------------------')
# print('---Operadores Aritmétricos---')
# Soma -> 10 + 5
# print(10 + 5)
# Subtração -> 5 - 2
# print(10 - 5)
# Divisão -> 10 / 2 -> Retorna float -> 5.0
# print(10 / 2)
# Divisão Inteira  -> 10 // 2 Retorna int -> 5
# print(10 // 2)
# Exponenciação -> 2 ** 10 -> 1024
# print(2 ** 10)
# Modulo -> Resto da divisão -> 25 % 2 -> Restro = 0 
# print(25 % 2)

# Exercício 2
# print('----------------------------------')
# print('--Exercício 2 -> IMC--')

# full_name = 'Helter Xavier'
# hight = 1.70
# peso = 67.5
# imc = peso / (hight * hight)

# print(f'{full_name}, seu IMC é de {imc}')

# print('----------------------------------')
# print('--Usuário digitar dados-')
# Usuário digitar um dado, input
# user_name = input('Qual é o seu nome ? ')
# print(f'O seu nome é {user_name}')

# OPERADORES CONDICIONAIS
# if -> SE
# elif -> SE NÃO SE
# ELSE -> SE NÃO

# horas = int(input('Que horas são?'));

# if horas < 12:
#   print('BOM DIA!!')
# elif horas >= 12 & horas >= 18:
#   print('BOM TARDE!!')
# elif horas >= 18 & horas > 5:
#   print('BOA NOITE!!')

# Operadores de comparação
# > -> maior
# maior = 2 > 1
# >= -> maior igual
# maior_igual = 2 >= 2
# < -> menor
# menor = 1 < 2
# <= -> menor igual
# menor_igual = 2 <= 2 
# == igual 
# igual= 'a' == 'a'
# != -> diferente
# diferente = 'a' != 'b'

# Exericio 3
# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')

# if primeiro_valor > segundo_valor: 
#   print(f'O {primeiro_valor=} é maior do que o {segundo_valor=}')
# else: 
#   print(f'p{segundo_valor=} é amior do que o {primeiro_valor=}')

#Operadore lógicos
# and (e) or (ou) not (não)
# and -> Todas as condições precisar ser verdadeiras
hora = 18
if hora >= 12 and hora <= 18:
  print('A hora está entre 12 horas e 18')
# or -> Qualquer condição verdadeira avalia toda a expressão como verdadeira
if hora >= 12 or hora <= 18:
  print('A hora está entre 12 horas 18 horas')
# not -> Usado para inverter expressões
if not 12:
  print('A hora está entre 12 horas 18 horas')