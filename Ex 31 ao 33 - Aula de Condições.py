# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando 0.50 por km para viagens de até 200km e 0,45 para viagens mais longas

from time import sleep
print(5*'-=-',5*'O',5*'-=-')
print('Bem vindo a companhia de viagens!')
print(5*'-=-',5*'O',5*'-=-')
a = int(input('\nQual a distância de sua viagem em Km? '))
print('Estamos processando sua informação...')
sleep(2)
print('Calculando a distância')
sleep(1)
if a > 200:
    b = a * 0.45
    print('A sua viagem de {} km custará {:.2f} R$'.format(a, b))
else:
    c = a * 0.50
    print('A sua viagem de {} km custará {:.2f} R$\n'.format(a, c))
print(15*"-=-")


# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date #importação do comando para detecção do ano atual
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year #comando para detectar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # 'and' acrescentou outra condição ao 'if', sendo ela que o módulo de 100 não pode ser diferente (!=) de zero
    #é a regra para um ano ser bissexto ser divisivel por 4, alguns anos divisiveis por 4 não são bissextos como os múltiplos de 100 e que não são mutilos de 400 ao mesmo tempo
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))


# Crie um programa que leia três valores e indique qual deles é o maior e qual deles é o menor
a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
if a > c and a > b:
    print('O maior valor é {}'.format(a))
if c > a and c > b:
    print('O maior valor é {}'.format(c))
if b > a and b > c:
    print('O maior valor é {}'.format(b))
if a < b and a < c:
    print('E o menor valor é {}'.format(a))
if b < c and b < a:
    print('E o menor valor é {}'.format(b))
if c < b and c < a:
    print('E o menor valor é {}'.format(c))
print(20*'-=-','\n')

# Forma mais simples para este exercicio
a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\n O maior número dentre estes é {}'.format(maior)) #a variavel vai mudar de acordo com a condição
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número dentre estes é {}'.format(menor))

# Ainda há uma terceira forma mais simples de ser usada
'''a = int(input('Digite um primeiro valor: '))
b = int(input('Digite um segundo valor: '))
c = int(input('Digite um terceiro valor: '))
numeros = [a, b, c]
print('O maior valor é {}'.format(max(numeros))
print('O menor valor é {}'.format(min(numeros))