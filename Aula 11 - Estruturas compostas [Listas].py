'''Listas são coleções de elementos entre colchetes, diferentes de tuplas são mutáveis. Assim como as tuplas, as listas
possuem alguns métodos úteis que são usados não apenas para identificar dados dentro dela mesma mas tbm para modifica-los
como:

lista.append(x) - > adiciona x na última posição da lista
lista.insert(0,x) - > adiciona x na indexação 0 da lista (pode modificar a indexação) e empurra todos os outros elementos adiante
lista.del[3] - > apaga o elemento da indexação 3 da lista
lista.pop(3) - > apaga o elemento da indexação 3 da lista (normalmente pop é usado para apagar o ultimo elemento da lista)
lista.remove(x) - > apaga o elemento de valor x (não é indice, pode ser a string ou o valor numerico)
lista.sort() - > ordena todos os valores em ordem crescente ou decrescente 'lista.sort(inverse=True)'
len(lista) - > mostra a quantidade de elementos que existem na lista

obs: a deleção d eum elemento rearranja a indexação dos itens na lista automaticamente

As listas podem ser criadas também a partir de ranges, como:

valores = list(range(4, 11)) - > cria uma lista chamada valores com os elementos 4 a 10, de idexação 0 a 6
'''

#Formas de demonstrar as repostas de uma lista:

valores = []
valores.append(5)
valores.append(2)
valores.append(4)
valores.append(9)
valores.append(7)

print(valores)

for v in valores:
    print('O valor é: {}'.format(v))

for c, v in enumerate(valores): #enumerate + a variavel c servem para tbm demonstrar as indexaçãoes na lista valores
    print('Encontrei o valor {} na indexação {} !'.format(v, c))

# Também é possível interagir diretamente com as listas através de inputs, da seguinte forma:

for count in range(0, 5):
    valores.append(int(input('Digite um novo valor para a lista: '))) #input pode ficar dentro do append e do insert
print(valores)

'''Se duas listas se igualares elas ficaram ligadas e modificar uma irá modificar diretamente a outra, esta ocorrência pode
ser vista da seguinte forma:

a = [2, 3, 4, 5, 6, 7]
b = a
b[2] = 8 - > essa modificação no indice 2 para valor 8 irá afetar ambas as listas, não só b, pois 'b' é 'a' e 'a' é 'b'

Se ocorrer de os valores de a serem jogados em b, este vinculo não é criado:

b = a[:] - > o colchete sem valores indica todos os valores de a'''


### Segunda parte - [Listas] ###

'''É possível criar listas aninhadas, ou seja, listas dentro de listas, neste caso uma lista inicial com 2 elementos e 
que apresenta a indexação 0 e 1, ao ser aninhada em outra lista, vai se o elemento de index 0 dessa nova lista, ou seja, 
a lista inicial representa apenas um elemento da segunda lista, por isso cobre apenas um index, enquanto a lista inicial 
possui dois index por possuir dois elementos. Exemplo:

pessoas = []
dados = ['pedro', 25]

pessoas.append(dados[:]) - > inserindo a lista dados na lista pessoa

Na lista dados:
pedro - > index 0
25 - > index 1

Na lista pessoas:
['pedro', 25] - > index 0

A lista pode ser escrita da seguinte forma:
pessoas = [['pedro', 25], ['maria', 18], ['joão', 32]]

print(pessoas[0][0]) - > dentor do indice 0 em pessoas, o item 0, netse caso 'pedro' que esta na indexação 0, da lista inicial
que por sua vez é a lista de indice 0 da lista mãe 'pessoas'. caso fosse [1][1] seria 18, [2][0] seria joão. Caso eu digite apenas
pessoas[1] irá ser mostrada a lista inteira ['maria', 19].Ou seja, os colchetes vão da designação macro para micro.
'''

teste = []
teste.append('Jorge')
teste.append(25)
print(teste)
galera = []
galera.append(teste[:]) #caso nãos eja colocado o [:] que faz uma copia e não uma correspondencia, as listas vão ser editadas concomitantemente e não individualmente
teste[0] = 'maria' #modifiquei a lista original, mas como criei uma copia em galera, os dados anteriores estão salvos
teste[1] = 22
galera.append(teste[:]) #adicionei uma copia da nova lista 'teste' em galera
print(teste) #irão aparecer as duas listas, jorge e maria.

galera = [['pedro', 25], ['maria', 18], ['joão', 32]]
for pessoa in galera:
    print(pessoa) #vai printar cada lista interna
    print(pessoa[0]) #vai printar só as indexações 0, no caos os nomes
    print('{} tem {} anos'.format(pessoa[0], pessoa[1]))

galera1 = []
dado = []
for c in range(0, 5):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #adicionando copia de dado em galera1, se n fizer isso, galera e dado serão correspondente e o clear ao final limpará ambos
    dado.clear()  #limpando a lista dado para novo registro, caso n seja limpa, ela irá ficar adicionando informações duplicadas em galera1
print(galera1)

for pessoa in galera:
    if pessoa[1] >= 21:
        print('{} é maior de idade'.format(pessoa[0]))