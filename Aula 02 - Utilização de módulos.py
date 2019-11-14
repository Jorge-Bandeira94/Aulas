'''Assim como alimentos que o corpo humano adiquire do meio externo, a linguagem python pode tbm usar de elementos externos para serem 
incluídos na produção de um script. Estas adições são as chamadas bibliotecas, um conjunto de elementos externos que poderão ser 
importados para a programação

Para importar estes elementos utilizamos o comando 'import' no começo do script com o nome do módulo / biblioteca à ser importada.
No caso de importar elementos únicos que estão dentro das bibliotecas a ordem se inverte para 'from nomedomodulo import alvo'. Caso
hajam mais alvos a serem importados deve-se separa-los por virgula.'''

import math #Ao usar este import, tenho acesso a várias funcionalidades das bibliotecas de matemática
num = (int(input('Digite um número ')))
raiz = math.sqrt(num) #Tendo importado a biblioteca math, ao digita o ponto, irão aparecer variadas funções diferentes que podem ser utilizadas adivinda da biblioteca
print('A raíz de {} é igual à {}'.format(num, raiz))
print('A raiz arredondada de {} é {}'.format(num, math.ceil(raiz))) #'ceil' é a função de arredondamento para cima, e 'floor' para baixo

# Antes de digitar a funcionalidade 'sqrt', caso queira ver todas as funcionalidades que podem ser importadas, basta apertar ctrl + espaço

from math import sqrt, ceil
num = (int(input('Digite um número ')))
raiz = math.sqrt(num)
print('A raíz de {} é igual à {}'.format(num, raiz))
print('A raiz arredondada de {} é {}'.format(num, math.ceil(raiz)))

import random
num = random.random() # randomiza um numero float entre 0 e 1, para inteiros digitar .randint(1, 10). Os número dentro dos parenteses são 
# os limites da randomização
print(num)

''' É possível verificar as bibliotecas que podem ser importadas utilizando ctrl + espaço depois do 'import'. Através da aba PyPi no site 
do Python é possível encontrar outras bibliotecas que podem ser baixadas para serem utilizadas. As biliotecas que já vem com o python são 
as chamdas built-in. É possível intalar bibliotecas diretamente pelo PyCharm da seguinte forma:

import emoji (biblioteca que não tenho). Vai aparecer uma lâmapada vermelha em cima do termo emoji, basta clicar nela e selecionar a 
instalação da biblioteca. Na parte inferior do pycharm vai aparecer que a biblioteca estará sendo instalada.'''

import emoji
print(emoji.emojize('Olá mundo :ghost:', use_aliases=True))

