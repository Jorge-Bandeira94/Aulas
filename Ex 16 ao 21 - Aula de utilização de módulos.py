# Crie um programa que leia um número na tela e apresenta apenas sua parte inteira
import math
a = float(input('Digite um número com casas decimais '))
print('A parte inteira de {} é {}'.format(a, math.trunc(a))) # Também é possível em vez de usar a função math.trunc(), usar a função int(), não necessitando importar a biblioteca math
print(40 * '=')


#Faça um programa que leia o comprimento dos catetos de um triângulo e calcule sua hipotenusa
catopo = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
# Da forma tardicional, usando o calculo inteiro fariamos da seguinte forma:
#hipot = catopo **2 + catad**2
#hipot2 = hipot **(1/2)
#print('O valor da hipotenusa é {}'.format(hipot2))

valor = math.hypot(catopo, catad) # Esta calculando a soma do quadrado dos catetos e igualando ao quadrado da hipotenusa, e posteriormente tirando sua raiz quadrada
print('A hipotenusa deste triângulo é {:.2f}'.format(valor))
print(40 * '=')


# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente deste ângulo
ang = float(input('Digite o valor do ângulo: '))
# O python le os graus em radianos, então deve haver uma conversão do input para radianos
co = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Os valores deste ângulo são: \n{:.3f} Para seno\n{:.3f} Para Coseno\n{:.3f} Para tangente'.format(sen, co, tang))
print(40 * '=')


# Faça um programa que sortei um entre quatro nomes
import random
#s = input('Digite o primeiro nome ')
#s1 = input('Digite o segundo nome ')
#s2 = input('Digite o terceiro nome ')
#s3 = input('Digite o quarto nome ')
#sort = random.choice([s, s1, s2, s3]) #o comando choice sorteou aleatoriamento uma variável
#print('O nome sorteado foi {}'.format(sort))

#Outra forma mais simples de fazer o mesmo sorteio
s = input('Digite o primeiro nome ')
s1 = input('Digite o segundo nome ')
s2 = input('Digite o terceiro nome ')
s3 = input('Digite o quarto nome ')
lista = [s, s1, s2, s3] #criar uma lista com as variaveis
escolhido = random.choice(lista) #usar o choice dentro da lista
print('O aluno escolhido foi {}'.format(escolhido))
print(40 * '=')


# Faça um programa que escolha aleatoriamente a ordem de apresentação de quatro alunos
import random
e = input('Digite o primeiro nome ')
e1 = input('Digite o segundo nome ')
e2 = input('Digite o terceiro nome ')
e3 = input('Digite o quarto nome ')
lista = [e, e1, e2, e3]
random.shuffle(lista)
print('A ordem de apresentação será{}'.format(lista))
print(40 * '=')

# Faça um programa que abra e reproduza um arquivo mp3
# Inicalmente deve-se ter o arquivo de música na mesma pasta dos seus arquivos de script python, utilizaremos o módulod e jogos pygame para importar musicas
import pygame
#Este módulo tem manual com regras e é bom lê-lo para saber como usa-lo
pygame.mixer.init #iniciar o mixer
pygame.init() #iniciar a biblioteca do pygame, vamos suar o mixer
pygame.mixer.music.load('ex022.mp3')
pygame.mixer.music.play() #iniciar a música
pygame.event.wait() #esperar a musica terminar

# Por algum motivo estes comandos não tocam a musica, a música só começou a funcionar após usar os comandos a seguir:

import pygame
mixer.init()
mixer.music.load('ex022.mp3')
mixer.music.play()
while mixer.music.get_busy(): #Estas duas linhas de comando estão mantendo o funcionamento da música
    time.Clock().tick(10)
