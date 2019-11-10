'''Diferente de 'for in range' que precisa d eum limite, a palavra 'while' não possui limites a não ser a exceção que o
programador impõem a ela, não sendo um limite numérico fixado como em 'for in range(). Esta é uma estrutura de repetição com
teste lógico.

Exemplo: um personagem precisa andar uma reta esburaca até chegar à maçã

while not apple: #enquanto não houver maçã, o boneco faz a repetição de ocmando do bloco abaixo, ao chegar, ele pega a maçã
    if chaonafrente:
        passo
    if buraco:
        pule
    if tivermoeda:
        pegue
pega

'''

r = 'S'
while r == 'S': #enquanto r for S, o programa continuara no loop
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
print('Fim')

import random
s = 0
pares = 0
impares = 0
while s != 12:
    s = random.randint(0, 20) #o while só irá parara quando a maquina randomizar um numero entre 0 e 20 que seja 12
    print('Randomicamente foi gerado o número {}'.format(s))
    if s % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print('Houveram {} números pares e {} números impares enquanto chegávamos à resposta.'.format(pares, impares))

