#Crie um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

numero = int(input('Digite um número inteiro'))
a = numero - 1
b = numero + 1
print('Seu antecessor é {}, e seu sucessor é {}'.format(a, b))
# Ou print('Seu antecessor é {}, e seu sucessor é {}'.format((numero + 1), (numero - 1))), este segundo caso é utilizável se não for precisar
# usar estes dados muitas vezes. O ideal é sempre referenciar valores à variáveis. Quanto menos utiliza-se variáveis, mais memória é economizada

numero2 = int(input('Digite outro número inteiro'))
c = numero2 * 2 #O dobro
d = numero2 * 3 #O triplo
e = numero2**(1/2) #A raíz quadrada
print('Seu dobro é {}'.format(c))
print('Seu triplo é {}'.format(d))
print('Sua raíz quadrada é {:.3f}'.format(e)) # Também é possível fazer o cálculo dentro do .format() como no exemplo anterior, basta abrir parenteses e colocar a operação com sua svariáveis
print(40 * '=')


#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nome = input('Digite o nome do aluno ')
print('Agora digite as notas de {}'.format (nome))
nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota'))
f = (nota1 + nota2) / 2 # Os parenteses tem precedencia 1, sendo a primeiera parte a ser resolvida, e para a operação resulta corretamente é necessário que a soma seja feito primeiro para que só depois o resultado seja dividido
# Caso não seja assim, a nota2 seria dividida primeiro por 2 e só depois seria somada à nota1
print(' A média final do aluno {} foi {}'.format(nome, f))
print(40 * '=')


#Desenvolva um programa que leia um valor em metros e apresente ele convertido em centímetros, em milímetros e nas demais medidas
g = float(input('Digite uma distância em metros '))
km = g / 1000
hec = g / 100
dec = g / 10
dcm = g * 10
cm = g * 100
mm = g * 1000
print('As medidas para a metragem {} \nem km são {}\nem hectâmetros são {}\nem decâmtros são {}\nem decímetros são {:.0f}\nem centímetros são {:.0f}\ne em milímetros são {:.0f}'.format(g, km, hec, dec, dcm, cm, mm))

