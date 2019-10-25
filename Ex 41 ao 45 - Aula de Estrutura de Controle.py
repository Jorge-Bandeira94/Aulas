# Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoriade acordo com a idade, ate 9 anos mirim, ate 14 infantil
# até 19 junior, ate 20 senior, acima master
from datetime import date

'''a = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
b = a - ano
c = abs(b)
if c <= 9:
    print('Atleta Mirim!')
elif 9 < c <= 14:
    print('Atleta Infantil!')
elif 14 < c <= 19:
    print('Atleta Junior!')
elif ano < a:
    print('Opção inválida')
else:
    print('Atleta Sênior!')'''

# Refaça o desafio 35 acrescentando o recurso de mostrar que tipo de triângulo está sendo formado: equilatero, isóceles ou escaleno
l1 = int(input('Digite o primeiro segmento do triângulo: '))
l2 = int(input('Digite o segundo segmneto do triângulo: '))
l3 = int(input('Digite o terceiro segmento do triângulo: '))
if abs(l1 - l2) < l3 < l1 + l2:
    print('Este triângulo pode existir com as medidas {}, {} e {}'.format(l1, l2, l3))
    if l1 == l2 and l1 == l3:
        print('Além disto, este triângulo é equilátero!')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Além disto, este triângulo é isóceles!')
    else:
        print('Além disto, este triângulo é escaleno!')

else:
    print('Este triângulo não pode existir com as medidas {}, {} e {}'.format(l1, l2, l3))

#