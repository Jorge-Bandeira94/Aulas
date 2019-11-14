# fAÇA UM PROGRAMA QUE LEIA CINCO VALORES NUMÉRICOS e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor
#digitado e suas posições
lista1 = []
listaM = []
listam = []
maior = 0
menor = 0
for i in range(0, 4) :
    a = int(input('Digite um número: '))
    lista1.append(a)
    if maior == 0 and menor == 0:
        maior = a
        menor = a
    if a > maior :
        maior = a
    if a < menor :
        menor = a
for i, v in enumerate(lista1):
    if maior == v :
        listaM.append(i)
    if menor == v :
        listam.append(i)
print('A lista de valores é {}, sendo o maior valor {} nas posições {} e o menor {}, nas posições {}'.format(lista1, maior, listaM, menor, listam))

# Crie um programa onde o usuário pode criar varios valores numericos e cadastre-os numa lista, caso o número ja exista
#ele não é adicionado, no final são exibidos todos os valores únicos digitados em ordem crescente.

lista2 = []
continuar = 'S'
while continuar == 'S':
    b = int(input('Digite um valor: '))
    if b not in lista2:
        lista2.append(b)
    continuar = input('Deseja continuar? [S/N] ').upper()
lista2.sort() #este sorte n funciona dentro de variavel, o fato de usa-loa qui ja remdula a lista2, por isso posos usa-la ja no format()
print('A lista em ordem crescente dos itens digitados é: {}'.format(lista2))

# Crie um programa onde o usuário digita 5 valores numericos e cadastre-os em uma lista, ja na posição corrte sem usar
# .sort(), no final mostre a lista ordenada na tela
lista8 = []
for a in range(0, 5):
    b = int(input('Digite um valor:'))
    if a == 0: # se a for a primeira indexação então executa esse bloco e grava o primeiro valor
        lista8.append(b)
    elif b > lista8[len(lista8)-1]: #se b for maior que o ultimo elemento da lista(por isso len total -1), ele é adicionado no final
        lista8.append(b)
    else:
        pos = 0 #cricei um contador pra ir andando dentro da lista
        while pos < len(lista8): #o while vai da indexação 0 até a ultima conforme o contador aumenta
            if b <= lista8[pos]: #verificando se b é menor ou igual a lista na posição pos, se for, o valor é inserido numa posição especifica
                lista8.insert(pos, b)
                break
            pos += 1 #contador aumentando, para ir andando dentro da lista
print('Os valores digitados em ordem foram {}'.format(lista8))

#Crie um programa que leia varios numeros e coloque numa lista, depois disso mostre os numeros digitas, a lista em formato
#decrescente e se o valor 5 foi digitado e está ou não na lista
lista4 = []
continuar1 = 'S'
while continuar1 == 'S':
    d = int(input('Digite um valor: '))
    lista4.append(d)
    continuar1 = input('Deseja continuar? [S/N] ').upper()
print('Os números digitados foram ', end='')
for n in lista4:
    print('...{} '.format(n), end='')
lista4.sort(reverse=True)
print('\nA lista em forma descrescente é: ', lista4)
if 5 in lista4:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está presente na lista')


# Crie um programa que irá ler varios numero se coloca-los numa lista, depois disso crie duas listas extras que vão conter
#apenas os valores pares e os valores impares digitados, ao final mostre o conteúdo das três listas geradas
lista5 = []
listap = []
listai = []

continuar2 = 'S'
while continuar2 == 'S':
    e = int(input('Digite um valor: '))
    lista5.append(e)
    continuar2 = input('Deseja continuar? [S/N] ').upper()
for n in lista5:
    if n % 2 == 0:
        listap.append(e)
    else:
        listai.append(e)

print('A lista completa é {}\nA lista de pares é {}\nA lista de impares é {}'.format(lista5, listap, listai))

#Este exercicio tbm pode ser feito de outra forma

'''lista5 = []
listap = []
listai = []

continuar2 = 'S'
while continuar2 == 'S' :
    e = int(input('Digite um valor: '))
    lista5.append(e)
    continuar2 = input('Deseja continuar? [S/N] ').upper()
for n in lista5: # a forma mais simples é adicionar tudo de uma vez com if ja dentor do laço, fiz desta forma alternativa para demonstrar novas possibilidades
    if n % 2 == 0 :
        listap.append(n)
    else :
        listai.append(n)

print('A lista completa é {}\nA lista de pares é {}\nA lista de impares é {}'.format(lista5, listap, listai))'''

# Crie um programa em que o usuário digite uma expressão que use parenteses. Seu aplicativo deverá  analisar se
# a expressão passada está com os parenteses abertos e fechados na ordem correta

expr = input('Digite a expressão: ')
pilha = []
for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop() #remover ultimo elemento
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')

''' Neste exercicio, o parentese que fecha elimita o que abre a partir do .pop quando ja existe parenteses na pilha, se houver
um numero desigual de parenteses na pilha o pop vai fazer que sobre um parentese aberto e isso vai ocasionar o erro da expressão
caso o tamanhos eja 0 e seja adicionado o parentese fechando, por len(pilha) != 0  TBM IRA OCASIONAR ERRO'''

