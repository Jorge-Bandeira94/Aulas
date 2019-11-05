# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com uma pequena pausa de 1 segundo entre eles
'''
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz ano novo!')

# crie um programa que mostre na tela todos os número pares que estão no intervalo entre 1 e 50
lista1 = []
for pares in range(1, 51):
    if pares % 2 == 0:
        lista1.append(pares)
print(lista1)

# Faça um programa que calcule a soma de todos os numeros impares que são multiplos de 3 e se encontram entre 1 e 500
s = 0
for i in range(1, 500):
    if i % 2 != 0:
        if i % 3 == 0:
            s = s + i
print(s)


# Refaça o desafio 09 (tabuada) utilizando repetições do laço for.
a = int(input('Digite um número: '))
for i in range(0, 11):
    b = i * a
    print(' A tabuada de multiplicação de {} por {} é {}'.format(a, i, b))

# Desenvolva um programa que leia seis numeros inteiros e mostre a soma daqueles apenas que forem pares . Se o valor digitado for impar desconsider-o
c = 0
for i in range(0, 6):
    a = int(input('Digite um número: '))
    if a % 2 == 0:
        c = c + a
print('A soma dos números pares digitados é {}'.format(c))

# Desenvola um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progessão
a1 = int(input('Digite um termo: '))
a2 = int(input('Digite a razão: '))
a3 = a1 + 10
for i in range(a1, a3, a2):
    print(i)


# Faça um programa que leia um numero inteiro e diga se ele é ou não um número primo
b1 = int(input('Digite um número: '))

if b1 == 2 or b1 == 3:
    print('Este número é primo')
elif b1 % 2 == 0 or b1 % 3 == 0:
    print('Este número não é primo')
else:
    print('Este número é primo')
'''

# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo
