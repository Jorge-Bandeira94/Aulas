# Crie um programa que leia varios numeros interio pelo teclado, ele só irá para quando o usuário digitar o valor 999 que é
# a condição de parada. No final ele mostra quantos numeros foram digitados e a soma entre eles
soma = 0
quantidade = 0
c = 0
while c != 999:
    c = int(input('Digite um número: '))
    if c == 999:
        break
    soma += c
    quantidade += 1
print(' A soma de todos estes números é {} e a quantidade de números digitados foi {}'.format(soma, quantidade))

# Faça um programa de tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuário. O programa será interompido quando o numero solicitado for negativo
print(23*'=', 'Tabuada', 23*'=')
a = 0
while a >= 0:
    a = int(input('Digite um número: '))
    if a < 0:
        break
    print(20*'=','A tabuada de {} é'.format(a), 20*'=' )
    for num in range(1, 11):
        print('{} x {} = {}'.format(a, num, a*num))
    print(57*'=')
print('Fim')


# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido  quando o jogador perder, mostrando o total de vitorias consecutivos que ele
# conquistou ao longo do logo.
import random
contador = 0
while True:
    computador = random.randint(0, 10)
    escolha = input('Escolha par ou ímpar [P/I]: ').upper()
    jogador = int(input('Jogue seu valor: '))
    if escolha == 'P':
        if (jogador + computador) % 2 == 0:
            print('Computador jogou {} e você jogou {}, sendo você {}, Você venceu!'.format(computador, jogador, escolha))
            contador += 1
        else:
            print('Computador jogou {} e você jogou {}, sendo você {}, Você perdeu!'.format(computador, jogador, escolha))
            break
    if escolha == 'I':
        if (jogador + computador) % 2 != 0:
            print(
                'Computador jogou {} e você jogou {}, sendo você {}, Você venceu!'.format(computador, jogador, escolha))
            contador += 1
        else:
            print('Computador jogou {} e você jogou {}, sendo você {}, Você perdeu!'.format(computador, jogador, escolha))
print('Você obteve {} vitórias consecutivas. Fim!'.format(contador))

# Crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o computador deve perguntar se o usuário quer
# continuar ou não. No final mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos
# de 20 anos
maisde18 = 0
homens = 0
menosdevinteMulheres = 0
continuacao = 'S'
while continuacao == 'S':
    sex = input('Digite o sexo desta pessoa [M/F]: ').upper()
    idade = int(input('Digite a idade desta pessoa: '))
    if idade >= 18:
        maisde18 += 1
    if sex == 'M':
        homens += 1
    if sex == 'F' and idade < 20:
        menosdevinteMulheres += 1
    continuacao = input('Deseja continuar? [S/N]: ').upper()
print('Foram cadastradas {} pessoa(s) maior(es) de 18 anos, das quais {} homem(s) e {} mulher(es) menor(es) de 20 anos.'.format(maisde18, homens, menosdevinte))

# Crie um programa que leia o nome e o preço de um produto, o programa irá perguntar se o usuário quer continuar. No final mostre o total
#gasto na compra, quantos produtos custam mais de 1000 reais e o nome do produto mais barato
maisdemil = 0
total = 0
barato = ''
baratopreco = 0
while True:
    produto = input('Qual nome do produto? ')
    preco = float(input('Qual seu preço: '))
    total = total + preco
    if barato == '' and baratopreco ==0:
        barato = produto
        baratopreco = preco
    if preco >= 1000:
        maisdemil += 1
    if preco < baratopreco:
        baratopreco = preco
        barato = produto
    a = input('Deseja continua? [S/N] ').upper()
    if a == 'S':
        continue
    else:
        break
print('Você comprou {} produtos com preço maior que R$ 1000 reais, com um total de R$ {} à pagar, sendo o produto mais barato {}, custando R$ {} '.format(maisdemil, total, barato, baratopreco))

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual o valor a ser sacado
# e o programa ira informar qunatas cedulas de cada valor será entregue, considerando cedulas de 50, 20, 10 e 1 reais
valor = int(input('Escolha o valor à ser sacado: R$ '))
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
total = valor
count50 = 0
count20 = 0
count10 = 0
count1 = 0
while True:
    if ced50 <= total:
        total = total - ced50
        count50 += 1
    else:
        if ced20 <= total:
            total = total - ced20
            count20 += 1
        else:
            if ced10 <= total:
                total = total - ced10
                count10 += 1
            else:
                if ced1 <= total:
                    total = total - ced1
                    count1 += 1
                else:
                    break

('Serão entregues {} cédulas de 50, {} cédulas de 20, {} cédulas de 10 e {} cédulas de 1'.format(count50,count20, count10, count1))
