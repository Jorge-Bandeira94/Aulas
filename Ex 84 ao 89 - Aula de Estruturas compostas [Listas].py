# Faça um programa que leia o nome e peso de varias pessoas e guarde tudo numa lista, no final mostre: quantas pessoas foram
# cadastradas, uma lista com as pessoas mais pesadas e uma lista com a pessoas mais leves

lista1 = 0
listageral =[]
listamae = []
listamax = []
listamin = []
continuar = 'S'
while continuar == 'S':
    nome = input('Digite o nome da pessoa: ')
    peso = int(input('Digite o valor do peso: '))
    listageral.append(nome)
    listageral.append(peso)
    lista1 += 1
    listamae.append(listageral[:])
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    listageral.clear() # seu eu n limpar a lista temporaria ela será adicionada duplicada em cada loop
for e in listamae :
    if e[1] > 99 :
        listamax.append(e[0])
    elif e[1] < 71 :
        listamin.append(e[0])
print('A quantidade de pessoas cadastradas foi {}, sendo as mais pesadas {} e as mais leves {}'.format(lista1, listamax, listamin))


'''Caso fosse necessário mostrar apena so maior e menor peso, seria feito um bloco da seguinte forma:
maior = 0
menor = 0
if maior == 0 and menor == 0:
    maior = listageral[1]
    menor = listageral[1]
else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
        
for p in listamae:
    if p[1] == maior:
        print('Os maiores pesos foram de {}'.format(p[0])
    if p[1] == menor:
        print('Os menores pesos foram de {}'.format(p[0])
        
Desta forma eu estaria mostrando apenas o maior e menor peso, e tbm as pessoas com pesos iguais caso empatassem no maior ou menor valor
        
'''
# Crie um programa onde o usuário possa digitar sete valores e cadastre-os numa lista única que mantenha separado os valores pares e ímpares
# no final mostre os valores pares e impares em ordem crescente

lista = []
listatemp = []
for c in range(0, 7):
    a = int(input('Digite um valor:'))
    listatemp.append(a)
    lista.append(listatemp[:])
    listatemp.clear()
a = list()
b = list()
for e in lista:
    for e1 in e:
        if e1 % 2 == 0:
            a.append(e1)
        else:
            b.append(e1)
lista.clear()
lista.append(a[:])
lista.append(b[:])
lista[0].sort()
lista[1].sort()
lista.sort()
print('A lista de núemros pares é {} e de ímpares é {}, que estão na lista {}'.format(lista[0], lista[1], lista))

'''Forma mais simplese correta

lista = [[], []]
for c in range(0, 7) :
    a = int(input('Digite um valor:'))
    if a % 2 == 0 :
        lista[0].append(a)
    else :
        lista[1].append(a)
''''

# Crie um programa que faça uma matriz 3x3  e preencha com valores lidos pelo teclado, no final mostre a matriz na tela, com a formatação correta
lista = [[],[],[],[],[],[],[],[],[]]
count = 0
for i in range(0, 9):
    valor = int(input('Digite o valor para a matriz: '))
    if lista[0] == 0:
        lista[0].append(valor)
        count += 1
    else:
        lista[count].append(valor)
        count += 1

print(lista[0],lista[1],lista[2],'\n',lista[3],lista[4], lista[5], '\n', lista[6], lista[7], lista[8])

'''forma mais simples
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range(0, 3): #estes dois laços vão colocar cada valor que eu digitar na linah e coluna respectva do range
        matriz[linha][coluna] = int(input('Digite um valor para a posição [{}/{}]: '.format(linha, coluna)))
for linha in range(0, 3): #estes dois laços irão printar o valores da forma formatada centralizada com 4 casas decimais.
    for coluna in range(0, 3): #ao encerrar o range de 0 a 3, o printa fora do bloco ira quebrar a linha, então a segunda linha começando embaixo vai de 0 a 3 de novo e asism sucessivamente
        print('[{:^4}]'.format(matriz[linha][coluna]), end='')
    print()
print(matriz)'''

# Aprimore o desafio anterior mostrando no final a soma de todos os valores pares, a soma dos valores da terceira coluna e
# o maior valor da segunda linha
pares = 0
terceira = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3): #estes dois laços vão colocar cada valor que eu digitar na linah e coluna respectva do range
        matriz[linha][coluna] = int(input('Digite um valor para a posição [{}/{}]: '.format(linha, coluna)))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        if linha == 1:
            maior = matriz[linha][coluna]
            if maior < matriz[linha][coluna]:
                maior = matriz[linha][coluna]
terceira = matriz[2][2] + matriz[1][2] + matriz[0][2] #ou poderia fazer um -> for linha in range (0, 3 ): terceira = terceira + matriz[linha][2]

for linha in range(0, 3): #estes dois laços irão printar o valores da forma formatada centralizada com 4 casas decimais.
    for coluna in range(0, 3): #ao encerrar o range de 0 a 3, o printa fora do bloco ira quebrar a linha, então a segunda linha começando embaixo vai de 0 a 3 de novo e asism sucessivamente
        print('[{:^4}]'.format(matriz[linha][coluna]), end='')
    print()

print(matriz)
print('A soma dos números pares é {}'.format(pares))
print('A soma dos valores da última coluna é {}'.format(terceira))
print('O maior vlaor da segunda linha é {}'.format(maior))


# faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear seis numeros entre 1 e 60, para cada jogo cadastrado, tudo em uma lista composta

import random
from time import sleep
contador = 0
lista = []
listatemp = []
print(10 * '=', 'Palpites de Loteria', 10 * '=')
b = int(input('Quantos jogos você deseja sortear? '))
print(41 * '=')
while b > contador:
    while len(listatemp) < 6:
        c = random.randint(1, 60)
        if c not in listatemp:
            listatemp.append(c)
        else:
            contador = contador
    lista.append(listatemp[:])
    contador += 1 #atenção no contador, tive problemas por ele estar dentro do laço if, e isso fazia ele crescer antes do previsto
    listatemp.clear()
for elemento in lista:
    print(elemento)
    sleep(0.5)
print(41 * '=')
print('BOA SORTE!')


# Crie um programa que leia o nome de varios alunos e suas duas notas, guarde tudo em uma lista composta. No final
#mostre um boletin contendo a média de cada aluno e permita que o usuário posos verificar as notas de cada aluno

No = 0
lista = []
listatemp = []
continuar = 's'
print(20 * '=', 'Boletim Escolar', 20 * '=')

while continuar == 's':
    listatemp.append(input('Digite o nome do aluno: ').upper())
    listatemp.append(float(input('Digite a primeira nota: ')))
    listatemp.append(float(input('Digite a segunda nota: ')))
    listatemp.insert(0, No)
    No += 1
    media = (listatemp[2] + listatemp[3]) / 2
    listatemp.append(media)
    lista.append(listatemp[:])
    listatemp.clear()
    continuar = input('Deseja continuar? [S/N] ').strip().lower()
print(20 * '=')
print('No.   Nome      Média')

a = b = c = ''
for elemento in lista:
    print('{:<4} {:^8} {:>5}'.format(elemento[0], elemento[1], elemento[4]))
print(20 * '=')

detalhe = 0
while detalhe != 999:
    print('Deseja ver detalhes de algum aluno?')
    detalhe = int(input('Digite o No. do aluno, caso não queira, digite 999: '))
    if detalhe <= len(lista):
        print('Detalhes de {}, 1º Nota {}, 2º Nota {}'.format(lista[detalhe][1], lista[detalhe][2], lista[detalhe][3]))
print('FINALIZANDO...')

# tive dificuldades na linha 34 por que esqueci que poderia usar dois colchetes, um para achar a indexação do elemento e outr
# para achar a indexação dentor deste elemento