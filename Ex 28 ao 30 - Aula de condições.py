# Escreva um programa que faça o computador pensar um número inteiro entre 0 e 5 e peça para que o usuário
# tente descobrir qual foi o número escolhido pelo computado. O programa devera escrever na tela se o usuário
# venceu ou perdeu.
import random
from time import sleep #importar este método da biblioteca time para usar. O sleep faz o pc dormir por alguns segundos
b = random.randint(0, 5)
print(40*'-=-')
print('Irei pensar em um número entre 0 e 5, tente adivinha-lo!')
print(40*'-=-','\n\n')
a = int(input('Digite o número que você acha que pensei : '))
if a == b:
    print('Processando...')
    sleep(3) #esse comando diz quantos segundos o pc vai esperar para avançar para o proximo
    print('Parabéns, você acertou, o número era {}'.format(b))
else:
    print('Processando...')
    sleep(3)
    print('Que pena, você errou. O número era {} '.format(b))
print(40*'-=-','\n\n\n')


# Escreva um programa que leia a velocidade de um carro e se ele ulltrapassar 80km/h, mostre uma msg dizendo que ele foi multado
# A multa vai custar 7 reais a cada km acima do limite, calcular essa multa

print('O radar eletrônico esta detectando a velocidade do carro em questão, aguarde...')
sleep(3)
v = random.randint(1, 120) #numero randomico de velocidade do carro
m = v - 80 #será usado caso a velocidade seja maior que 80, nunca será um numero negativo desta forma
valor = m * 7 #o resultado de m será multiplicado pelo valor de cada km/h acima do permitido
if v > 80:
    print('O carro estava à {} km/h, {} km/h acima do limite, a multa para esta infração será de {} R$'.format(v, m, valor))
else:
    print('O carro estava em velocidade de {} km/h, dentro do limite.'.format(v))
print('---Fim---\n\n')



# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
num = int(input('Digite um número inteiro: '))
resultado = num % 2 #o resto da divisão (%) de um número par por 2 é sempre 0, de um numero impar é sempre 1, são constantes
if resultado == 1:
    print('O número digitado é IMPAR!')
else:
    print('O número digitado é PAR!')