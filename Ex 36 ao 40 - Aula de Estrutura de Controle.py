# Crie um programa para aprovar um emprestimo bancario para a compra de uma casa, O programa vai perguntar
# o valor da casa, o slário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
# que ela não pode exceder 30% do salário ou então oo emprestimo será negado

casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Agora especifique o salário do comprador: R$ '))
anos = int(input('Em quantos anos deseja parcelar? '))
mês = anos * 12
prestação = casa / mês
if prestação > (salario * 30 / 100):
    print('Infelizmente este parcelamento não poderá ser efetuado')
else:
    print('Sua parcela irá custar {:.2f} por mês'.format(prestação))
print(20*'-=-', '\n')

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal

print(20*'-=-', '\n')
# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais

a = int(input('Digite um número inteiro: '))
b = int(input('Digite um segundo número inteiro: '))
if a > b:
    print('O maior número dentre os dois é {}!'.format(a))
elif a < b:
    print('O maior número entre os dois é {}!'.format(b))
else:
    print('Ambos são iguais')
print(20*'-=-', '\n')

# Faça um programa que leia o ano de nascimento de um jovem e informe, de cordo com sua idade:
# se ele ainda vai se alistar no serviço militar, se é hora de se alistar, se ja passou do tempo de alistamento
# seu programa também deve mostrar o tempo que falta ou que passou do prazo

from datetime import date
a = (int(input('Digite seu ano de nascimento: ')))
a1 = int(input('Digite sua idade: '))
b = date.today().year
if b - a < 18:
    c = 18 - a1
    print('Você irá se alistar em {} anos'.format(c))
elif b - a == 18:
    print('Seu alistamente ocorrerá neste ano!')
else:
    d = a1 - 18
    print('Seu alistamente deveria ter sido efetuado à {} anos atrás'.format(d))


# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida: abaixo de 5 reprovado, entre 5 e 6.9 recuperação, superior a 7 aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5.0:
    print('Reprovado com nota {:.2f}'.format(média))
elif 5.0 <= média <= 6.9: #se eu não colocar <= o programa n entendera que uma média 5 pode causar recuperação
    print('Recuperação com média {:.2f}'.format(média))
else:
    print('Aprovado com média {:.2f}'.format(média))