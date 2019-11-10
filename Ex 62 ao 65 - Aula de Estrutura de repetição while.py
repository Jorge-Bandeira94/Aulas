# Faça um programa que receba um numero e uma razão e retorne sua PA usando while e que mostre os 10 primeiros termos
a = int(input('Digite um número: '))
b = int(input('Digite a razão: '))
c = 0
m = 0
print(a, end= ' -> ')
while c < 10:
    c += 1
    a = a + b
    m += 1
    print(a, end= ' -> ')
print('FIM')
r = int(input('Deseja adicionar mais termos para serem apresentados à esta PA?, Caso sim, digite a quantidade, caso não, digite zero: '))
while r != 0:
    d = 0
    while d < r:
        d += 1
        a = a + b
        m += 1
        print(a, end= ' -> ')
    r = int(input('Deseja adicionar mais termos para serem apresentados à esta PA?, Caso sim, digite a quantidade, caso não, digite zero: '))
print('A progressão foi finalizada com {} termos mostrados'.format(m))
print('FIM')

# Faça um programa que mostre os X primeiro termos de uma sequencia de fibonacci
b = int(input('Digite quantos termos deseja que sejam mostrados: '))
c = 0
c1 = 0
c2 = 1
print(c1, '->', c2, end=' -> ')
while c < b:
    c += 1
    c3 = c1 + c2
    c1 = c2 #estas transformações fazem com que c1 que era 0 vire 1 e c2 que era um vire o resultado de 0 +1, quando omlanço retornar
    c2 = c3 # o c1 será 1, e o c2 será 2, que foi a soma de 1 + 1. Eu fiz a expressão andar de lado na coluna dos termos
    print(c3, end=' -> ')
print('FIM')

# Faça um programa que some todos os numeros que você digitar, e ao digitar 999 ele encerre o programa
a = int(input('Digite um número: '))
b = 0
c = 0
while a != 999:
    b = b + a
    c += 1
    a = int(input('Digite um número: '))
print('Você diigitou {} número e a soma dos números digitados foi {}'.format(c, b))

# Crie um programa que leia varios números inteiros e no final mostre a média entre todos os valores, e quais foram os maiores e os menores
# o programa deve perguntar ao usuário se ele quer ou não continuar.
a = int(input('Digite um valor: '))
c = 0 + a
d = 1
e = 'S'
max = a
min = a
e = str(input('Deseje continuar? [S/N] ')).upper().strip()
while e == 'S':
    a = int(input('Digite mais um valor: '))
    c += a
    d += 1
    e = str(input('Deseje continuar? [S/N] ')).upper().strip()
    if max < a:
        max = a
    if min > a:
        min = a
media = c / d
print('A média dos valores digitados foi {}'.format(media))
print('O número mais alto foi {} e o menor foi {}'.format(max, min))
