# Faça um programa que leia nome e média de um aluno, guardando a situação deste aluno em um dicionário. No final mostre o conteúdo na tela
'''
dict1 = {}
a = input('Digite o nome do aluno: ')
b = float(input('Agora digite a média: '))
dict1['nome'] = a
dict1['media'] = b
if b >= 7:
    dict1['situacao'] = 'Aprovado'
else:
    dict1['situacao'] = 'Reprovado'
print('O aluno {} encontra-se {}.'.format(dict1['nome'], dict1['situacao']))
'''

# Croe um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios, guarde todos os reusltados em um dict. No final
# coloque o dict em ordem sabendo quem será o vencedor que tirou o maior número.

from random import randint
from time import sleep
from operator import itemgetter # para o rankeamento
dict2 = {}

jogador1 = randint(1, 6)
dict2['jogador1'] = jogador1
print('O jogador 1 lançou {}'.format(dict2['jogador1']))
sleep(1)
jogador2 = randint(1, 6)
dict2['jogador2'] = jogador2
print('O jogador 2 lançou {}'.format(dict2['jogador2']))
sleep(1)
jogador3 = randint(1, 6)
dict2['jogador3'] = jogador3
print('O jogador 3 lançou {}'.format(dict2['jogador3']))
sleep(1)
jogador4 = randint(1, 6)
dict2['jogador4'] = jogador4
print('O jogador 4 lançou {}'.format(dict2['jogador4']))
sleep(1)

for k, v in dict2.items():
    print('O jogador {} tirou {}'.format(k, v))

ranking = sorted(dict2.items(), key=itemgetter(1), reverse = True) # O sorted() esta colocando os valores em ordem crescente dos itens de dict2 seguindo apenas as keys. O 1 é a indexação de onde esta o valor, o reverse vai reverter a ordem para maior > menor de valores
print(' O ranking de jogadores foi: \n 1º Lugar {} \n 2º Lugar {} \n 3º Lugar {} \n 4º Lugar {}'.format(ranking[0][0], ranking[1][0], ranking[2][0], ranking[3][0]))