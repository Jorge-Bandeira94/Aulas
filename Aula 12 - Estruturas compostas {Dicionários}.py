'''Dicionarios são estruturas de dados semelhante as listas e tuplas, mas com índices que podem ser literais, ou seja, pode
possuir nome ao invés de valores. São caracterizados pelas chaves dic = {}. As indexações dos dicionários são chamadas de
chaves, enquanto que os elemenots são os valores. Para associar os dados ao indices devemos fazer
da seguinte forma:

dic = {'nome' : 'pedro', 'idade': 25} - > onde nome e idade são as indexações 0 e 1 deste dicionário.
print(dados[nome]) - > o nome pedro sera printado

Caso não exista um elemento, diferente da função append, no dicionário usaremos:

dic['sexo'] = 'm' - > irá ser criada a indexação 'sexo' e nela será adicionado 'm' para pedro
del.dic['idade'] - > elimina o elemento idade
dic.values() - > retorna todos os valores escritos em cada index
dic.keys() - > retorna o nome de cada index
dic.items() -> retorna os valores e nome dos seus index
dic.copy() - > copia o dicionário para outro ou para uma lista, semelhante ao [:] nas listas

Obs: é importante lembrar que as keys devem estar também dentro de aspas, e sempre que eu pedi-las tbm devo coloca-las
em aspas como em dic['sexo'] ou print(dic['nome'])


exemplo prático:
'''
filmes = {'título':'Star Wars', 'ano':1987, 'Diretor':'George Lucas'}
for key, value in filmes.items():  #este .itens é como o enumerate das listas
    print('O {} é {}'.format(key, value))

'''Dicionários, listas e tuplas podem ficar um dentro do outro, por exemplo, posso criar uma lista chamada locadora e 
colocar vários dicionários diferentes dentro desta lista onde, para achar o dicionário desejado seria solicitado seu indice
da lista'''

Brasil = []
estado1 = {'uf': 'pernambuco', 'sigla': 'PE'}
estado2 = {'uf': 'são paulo', 'sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[1]['uf'])
print(Brasil[0]['sigla'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Digite o estado: ')
    estado['sigla'] = input('Digite a sigla do estado: ')
    brasil.append(estado.copy())   # Sem o .copy() só será adicionada as informações finais que são as que estaram no dict no momento final do loop
print(brasil)
for e in brasil:
    print(e)

