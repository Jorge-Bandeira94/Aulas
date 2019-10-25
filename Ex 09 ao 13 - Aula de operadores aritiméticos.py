# Crie um programa que leia um npumero inteiro qualquer e mostre na tela sua tabuada
numero = int(input('Digite um número '))
x = '=' * 10
z = '=' * 10
a = numero * 1
b = numero * 2
c = numero * 3
d = numero * 4
e = numero * 5
f = numero * 6
g = numero * 7
h = numero * 8
i = numero * 9
j = numero * 10

print('A tabuada de multiplicação para este número é\n{}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\n{}'.format(x, numero, a, numero, b, numero, c, numero, d, numero, e,  numero, f, numero, g,  numero, h, numero, i,  numero, j, z))
print(40 * '=')


# Outra forma de criar a tuabuada simplificada é a seguinte:

num = int(input("Digite um número"))
print('-' * 12)
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 10, num*10))
print('-' * 12)
print(40 * '=')


# É possível formatar o resultado para ficar graficamente mais bonito alinhado. Colocar :2 dentro dos colchetes vai fazer com que os números se alinhem em duas casa da seguinte form:

num = int(input("Digite um número"))
print('=' * 12)
print('{} x {:<2} = {}'.format(num, 1, num*1))
print('{} x {:<2} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('=' * 12)
print(40 * '=')


# Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar  com este dinheiro
dol = float(input('Quantos reais você possui para converter em outras moedas? R$'))
k = dol / 3.27
r1 = dol / 2.65
r2 = dol / 34088.39
r3 = dol / 4.61
print('Você terá {:.2f} U$,\n ou {:.2f} NZ$,\n {:.4f}, ou bitcoins,\n ou {:.2f} EU,\n utilizando {:.2f} R$'.format(k, r1, r2, r3, dol))
print(40 * '=')


#Crie um programa que que calcule a área de uma parede em metros e a quantidade de tinta necessária para pinta-la, sabendo que 1L de inta pinta 2 m²

p1 = float(input('Insira as medidas em metros de largura da parede '))
p2 = float(input('Insira as medidas em metros de altura da mesma parede '))
area = p1 * p2
tinta = area / 2
print('Sua parede possui as dimensões de {} x {} com área total de {} m²'.format(p1, p2, area))
print('Serão necessários {:.3f} litros de tinta para pintar esta parede que possui {} m²'.format(tinta, area))
print(40 * '=')


#Crie um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Insira o preço do produto. R$ '))
desconto = int(input('Insira o desconto . % '))
n = desconto / 100
m = produto - (produto * n)
o = n * 100
print('O novo preço deste produto com o desconto de {} % é {:.2f} R$'.format(o, m))
print(40 * '=')


# fAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO e calcule este salário com 15% de aumento
salario = float(input('Digite seu salário. R$'))
bonus = int(input('Digite a % de aumento. % '))
aumento = salario + (salario * (bonus/100))
print('Seu novo salário é de {} R$'.format(aumento))