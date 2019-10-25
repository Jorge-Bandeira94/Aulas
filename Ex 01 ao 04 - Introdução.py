print('Olá mundo!')

nome = input('Qual o seu nome?')
print ('Seja bem vindo' + nome)
Subject1 = input('Este é um curso introdutório, digite seu tipo de conhecimento')
print ('Começaremos o curso a partir do módulo 1 para' + Subject1)

##########################

#n1 = input('Digite um número')

#n2 = input('Digite mais um número')

#S = n1 + n2

#Este S esta fazendo uma concatenação e não uma soma, deve-se utilizar os tipos primitivos

#print('A soma resulta em', S)

#Para resolver este problema precisamos fazer com que o input deixe de ser considerado um string e sim um número,
#então usaremos o tipo primitivos int(número inteiro) [Há também o float(número com casas decimais), bool(True ou false)
# e str(String)], onde tudo que estiver dentro dos parenteses será considerado um numero inteiro, desta forma:

n1 = int(input('Digite um número'))

n2 = int(input('Digite mais um número'))

S = n1 + n2

# forma simples -> print('A soma vale ' S)

# forma simples trabalhosa -> print('A soma entre', n1, 'e', n2, 'vale', S)

#Outra forma de escrever o print: print('A soma vale {}'.format{S}) Onde os {} será a variavel dentro de .format{S}.
# Sendo uma boa forma de criar prints mais complexos.

print('A soma entre {} e {} vale {}'.format(n1, n2, S))

##########################

a1 = float(input('Digite um número'))
a2 = float(input('Digite mais um número'))
b = a1 + a2
print ('O resultado da soma entre {} e {} é {}'.format(a1, a2, b))

##########################

#a = input('Digite algum caractere ')
#print(a.isnumeric())
#print(a.isalpha())

#Exercicio para usar as funções 'is' que determinam se um caracter é falso ou verdadeiro para o tipo testado

a = input('Digite algum caractere ')
print(a.isnumeric())

##########################
a1 = input('Digite algo no teclado ')
print('Qual tipo primitivo deste valor?', type(a1))
print('É alfabético ?', a1.isalpha())
print('É um número?', a1.isnumeric())
print('É uma palavra em caixa alta?', a1.isupper())
print('É uma palavra toda em minúcsulo?', a1.islower())
print('Possui a primeira letra em maiúsculo?', a1.istitle()) #Capitalizado
print('É um número decimal?', a1.isdecimal())
print('Só tem espaços?', a1.isspace())
print('É alfanumérico?', a1.isalnum())

#a1 É um objeto, com características e funcionalidades, possuindo atributos e métodos, os
#parenteses no fim de cada 'is' indica que são métodos
