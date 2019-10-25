# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1250,00 calcule um aumento de 10%, para inferiores, 15%
s = float(input('Digite o valor de seu salário: R$ '))
if s > 1250.00:
    aumento1 = (s * 0.1)
    f1 = s + aumento1
    print('\nSeu novo salário com ajuste de 10 % é de {:.2f} R$, sofrendo um aumento de {:.2f} R$'.format(f1, aumento1))
else:
    aumento2 = (s * 0.15)
    f2 = s + aumento2
    print('\nSeu novo salário com ajuste de 15 % é de {:.2f} R$, sofrendo um aumento de {:.2f} R$'.format(f2, aumento2))
print(20*'-=-')

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um tirangulo.
from time import sleep
print('\n\n\nOlá!')
sleep(1)
print('Vamos tentar criar um triângulo? Digite a medida para cada segmento e verifique se é possível cria-lo...')
print(40*'-=-')
sleep(2)
r1 = float(input('\nDigite o tamanho do segmento A: '))
r2 = float(input('Digite o tamanho do segmento B: '))
r3 = float(input('Digite o tamanho do segmento C: '))
r4 = abs(r2 - r3)
if r4 < r1 < r2 + r3: #Condição de existencia do triangulo onde a soma de dois lados sempre tem que ser maior que um terceiro lado, a formula é |L1 - L2| < L3 < L1 + L2
    print('\nOs segmentos {}, {} e {} SÃO capazes de produzir um triângulo'.format(r1, r2, r3))
else:
    print('\nOs segmentos {}, {} e {} NÃO são capazes de produzir um triângulo'.format(r1, r2, r3))