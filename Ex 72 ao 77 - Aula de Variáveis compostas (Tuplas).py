# Crie um programa que tenha uma tupla totalmente preenchida por uma contagem por extenso de zero a 20. Seu programa vai
#ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.
tupla1 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
digite = int(input('Digite um valor entre 0 e 10: '))
while digite < 0 or digite > 10:
    print('Número não válido, tente novamente')
    digite = int(input('Digite um valor entre 0 e 10: '))
a = tupla1[digite]
print('Você digitou {}'.format(a))


# Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
# depois mostre a) apenas os cinco primeiros. b) os quatro ultimo c)uma lista com os times em ordem alfabética d)em que
#posição está a chapecoense.
tupla2 = ('Flamengo', 'Palmeiras', 'Santos','Grêmio','São Paulo','Athletico-PR','Internacional','Corinthians','Bahia','Goiás','Vasco','Atlético-MG','Fortaleza','Ceará','Cruzeiro','Fluminense','Botafogo',	'CSA','Chapecoense','Avaí')
print(tupla2[:5])
print(tupla2[-4:])
print(sorted(tupla2))
print('Chapecoense está na', tupla2.index('Chapecoense'), 'º posição')


# Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla. Depois disso mostre a listagem de números
#gerados e também indique o menor e o maior valor que estão na tupla
import random
list1 = []
max = 0
min = 0
for c in range(0, 5):
    a = random.randint(0, 10)
    list1.append(a)
    if max == 0 and min == 0:
        max = a
        min = a
    if a > max:
        max = a
    if a < min:
        min = a
b = tuple(list1)
print('A tupla é composta de {}. O maior valor é {} e o menor {}'.format(b, max, min))


#Desenvolva um programa que leia 4 valores e guarde-os numa tupla, depois mostre quantas vezes apareceu o valor 9, em que
#posição foi digitado o primeiro valor 3 e quais foram os numeros pares
lista2 = []
pares = []
for c in range(0, 4):
    a = int(input('Digite um valor: '))
    lista2.append(a)
    if a % 2 == 0:
        pares.append(a)
b = tuple(lista2)
d = tuple(pares)
print('O número 9 apareceu {} vezes'.format(b.count(9)))
if 3 in b:
    print('O valor 3 apareceu na posição {}'.format(b.index(3)))
else:
    print('O valor 3 não foi digitado')
print('Os números pares foram {}'.format(d))


# Crie uma lista de produtos e preços alinhados dentor de uma tupla
listagem = ('Lapis', 1.75, 'Borracha', 1.00, 'Caderno', 10.00, 'Lapiseira', 2.75, 'Papel Paltado', 3.00, 'Grampeador', 8.00)
print(10 * '=', 'Listagem de Preços', 10 * '=')

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>6.2f}')

# Crie um programa que tenha um tupla com varias palavras e depois mostre as vogais de cada palavra
palavras = ('Lapis', 'aprender', 'programar', 'linguagem', 'curso', 'mamona', 'berinjela', 'jatropha')
for p in palavras:
    print(p, 'contém as vogais: ', end='')
    for letra in p: #depois que a palavra é lida cada letra, é passado para proxima palavra
        if letra in 'aeiou': #fiz o if verificar cada letra de p, que por sua vez é cada palavra da tupla. Se esta letra estivesse dentro da string 'aeiou' ela seria printada. Os 'end=' fazem com que fiquem junto de sua palavra
            print(letra, end=' ')
