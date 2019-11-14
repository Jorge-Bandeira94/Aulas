''' Tuplas são variáveis (ou coleções) que guardam um ou mais valores, diferente de variáveis comuns que só guardam um valor, e caso outro
valor seja atribuido a elas, o anterior é esquecido. Os elementos da tupla são divididos por indices. Este conceito serve para as strings
também em que elas são consideradas variaveis compostas devido a serem indexadas. Exemplo:'''

lanche = ('sanduiche', 'pizza', 'suco', 'pudin')
print(lanche[3]) #-> pudin
print(lanche[0:2]) #-> Sanduiche, pizza
print(lanche[1:]) #-> pizza, suco, pudin
print(lanche[-1]) #-> pudin
print(lanche[-2]) #-> suco, pudin

'''Também podemos utilizar o método len para dizer quantos elementos há na variável lanche, exemplo:'''

print(len(lanche)) #-> 4

'''Os usos de estruturas de repetição também são úteis. Exemplo:'''

for c in lanche:
    print(c) #-> vai retornar cada elemento da tupla

for c in range(0, len(lanche)):
    print('Eu vou comer {}'.format(lanche[c])) # para imprimir o nome em c, preciso usar ele dentro de colchetes, se não só vai imprimir os indices

for posicao, comida in enumerate(lanche): #consigo o nome e o valor do indice
    print('Eu vou comer {}, de valor {}'.format(comida, posicao))

'''As tuplas são imutáveis, e não podem ter seus elementos alterados ou modificados. Apesar disto é possível apagar a tupla com del(tupla) '''

tupla1 = (1, 2, 3)
tupla2 = (2, 5, 1, 2)
tupla3 = tupla1 + tupla2 #irá gerar uma tupla com todos os elementos
print(tupla3)

'''Métodos úteis
tupla.count() #contará quantos (x) estarão dentro da tupla
tupla.index() #mostrara a indexação de (x) na primeira ocorrência
tupla.index(2, 5) #procura o numero 2 a partir da posição 5 (após a virgula está o deslocamento
'''


