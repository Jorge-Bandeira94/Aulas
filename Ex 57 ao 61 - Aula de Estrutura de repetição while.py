# Faça um programa que leia o sexo de uma pessoa, mas só aceite M ou F, se estiver errado peça digitação novamente até ter o valor correto.

b = input('Digite seu sexo [F/M]:').upper().strip()
while b != 'M' and b != 'F':
    print('Esta especificação não é valida, tente novamente.')
    b = input('Digite seu sexo [F/M]:').upper().strip()
print('Dados registrados com sucesso.')

#Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 a 10. Só que agora o jogador vai tentar adivinhas
#até acertar, mostrando no final quantos palpites foram necessários para vencer


import random
print(20*'-=-')
print('Irei pensar em um número entre 0 e 10, tente adivinhar !')
print(20*'-=-')
a = random.randint(0, 10)
c = 1
d = int(input('Em qual número pensei?: '))
while d != a:
    c += 1
    if d > a:
        print('Mais... tente novamente')
        d = int(input(''))
    else :
        print('Menos...tente novamente')
        d = int(input(''))
    if d == a :
    print('Parabéns, você acertou em {} tentativas, o número que pensei foi {}'.format(c, a))
print('FIM')


# Crie um programa que leia dois valores e mostre um menu na tela, [1] somar, [2] multiplicar, [3] maior entre os dois, [4] novos números
# [5] sair do programa. O programa deverá executar a operação solicitada em cada caso

a = float(input('Digite um valor: '))
b = float(input('Digite um segundo valor: '))
c = ''

while c != 5:
    print('Escolha uma opção: [1] Somar; [2] Multiplicar, [3] Maior entre os valores, [4] Novos números, [5] Fechar programa')
    c = int(input(''))
    if c == 1:
        print('O valor da soma será {}'.format(a+b))
    elif c == 2:
        print('O valor da multiplicação será {}'.format(a*b))
    elif c == 3:
        if a > b:
            print('O maior valor é {}'.format(a))
        else:
            print('O maior valor é {}'.format(b))
    elif c == 4:
        a = int(input('Digite o novo numero: '))
        b = int(input('Digite o segundo novo numero: '))
print('FIM')

# FAça um programa que leia um numero qualquer e mostre o seu fatorial, exemplo 5! = 5 X 4 X 3 X 2 X 1 = 125
from math import factorial

a = int(input('Digite um número qualquer: '))
f = factorial(a)
print('O fatorial de {} é {}'.format(a,f))

# sem o módulo math
a = int(input('Digite um número qualquer: '))
c = a
f1 = 1
print('Calculando {}! = '.format(a), end='')
while c > 0:
    print('{}'.format(c), end='') # o end= é para ser escrito tudo na mesma linha
    print(' x ' if c > 1 else ' = ', end='')
    f1 = f1 * c #aqui resolve o fatorial, onde cada numero no f1 vai multiplica o numero de c regressivo
    c -= 1
print('{}'.format(f1)) #como o ultimo print tem edn=, este vai aparecer junto a ele, e precisa estar fora do bloco para só aparecer no final do while

# Faça um programa que receba um numero e uma razão e retorne sua PA usando while e que mostre os 10 primeiros termos
a = int(input('Digite um número: '))
b = int(input('Digite a razão: '))
c = 0
print(a, end= ' -> ')
while c < 10:
    c += 1
    a = a + b
    print(a, end= ' -> ')
print('FIM')