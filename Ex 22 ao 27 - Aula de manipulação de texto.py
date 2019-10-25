# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1) O nome com todas as letras maiúsculas 2) com todas minúsculas, 3) quantas letras ao total (sem considerar os espaços 4) quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo')) #posso colocar a função .strip no fim desta linha de comando para eliminar possíveis espaços antes e depois do nome
print('Seu nome em maísculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
letras = nome.split()
junt = (''.join(letras))
tamanhotodo = (len(junt))
primeiro = letras[0]
tamanho = len(letras)
print('O primeiro nome é {} e possui'.format(primeiro), len(primeiro), 'letras')
print('A quantidade de letras neste nome é de {}'.format(tamanhotodo))

#pare resolver a questão da contagem sem os espaços, tbm pode-ser usar:
#print('Seu nome tem ao total {} letras'.formar(len(nome) - nome.count(' ')))   Neste caso ele irá contar os espaços e retira-los
print(40* '=')

# Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex: digite um numero: 1834
# unidade 4
# dezena 3
# centena 8
# milhar 1

num = int(input('Digite um número entre 0 e 9999 '))
#a1 = n.split()
#print('Este número se divide em\n{} Unidade\n{} Dezena\n{} Centena\n{} Milhar'.format(n[3], n[2], n[1], n[0]))
# Caso digite menos de quatro digitos ocorre erro, para lidar com isto usaremos metodos matemáticos
u = num // 1 % 10 # o numero será dividido inteiro por um e o resto de sua divisão por 10, será responspavel por resultar na unidade do digito
print('A unidade é {}'. format(u))
d = num // 10 % 10 # A cada nova divisão inteira, usar a casa de dezena, centena ou milhar
print("A dezena é {}".format(d))
c = num // 100 % 10
print('A centena é {}'.format(c))
m = num // 1000 % 10
print('O milhar é {}'.format(m))
# O principio é que o resto da divisão sempre vai ser o elemento que caracteriza a unidade,dezena,centena ou milhar.
# 1234 / 1 = 1234, então ele é dividido por 10 resultando em 123 e sobrando 4 no quociente da divisão, este quatro será a unidade capturada pelo %
# Para cada casa decimal a mais aumenta-se tbm a divisão inteira para que o modulo sempre consiga pegar a casa decimal correta
# 1234 / 10 = 123, onde a nova divisão de 123 por 10 resulta em 12 e sobram (3); 1234 / 100 = 12, a nova divisão de 12 por 10 resulta em um e sobram (2)
print('='*40)

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cid = str(input('Digite o nome de sua cidade: ')).strip() # O strip resolve o problema dos espaços
ma = cid.upper() # Joguei tudo pra maiusculo para mesmo que tenha sido digitado revezando entre caixa alta e minusculo a palavra fique inteiramente de uma forma, e esta forma vai ser usada para procura-la no input
dividido = ma.split()
start = ('SANTO' in dividido[0]) #Consegui fazer com que ele procurasse a palavra 'Santo' no indice 0 do split, que é a primeira palavra.
print('Esta cidade começa com "Santo"? {}'.format(start))
print('='*40)

# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('Digite seu nome completo: ')).strip()
'''no1 = nome.upper()  #dentro do format eu poderia colocar 'SILVA' in nome.upper em vez de criar uma linha de comando para cada variavel
r = ('SILVA' in no1)'''
print('Este nome possui a palavra Silva? {}'.format('silva' in nome.lower()))
print('='*40)

# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra A, em que posição ela aparece a primeira vez, e em que posição aparece pela ultima vez
tecl = str(input('Digite uma frase qualque: ')).strip()
up = tecl.upper() #precisa que o 'tecl' seja um str, ou não vai funcionar
letr = up.count('A')
print('A letra "a" aparece {} vezes em sua frase.'.format(letr))
pos = up.find('A') + 1 # Este mais um é para que o programa não retorne a posição 0, pra ficar esteticamente mais bonito
print('Esta letra aparece pela primeira vez na posição {}'.format(pos))
fin = up.rfind('A') + 1  #rfind procura do lado oposto (right)
print('Esta letra aparece pela última vez na posição {}'.format(fin))
print('='*40)

# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e ultimo nome separadamente
nome1 = str(input('Digite seu nome completo: ')).strip()
dividido = nome1.split()
primeiro1 = dividido[0]
ultimo1 = dividido[-1]
print('Seu primeiro nome é {} e seu último nome é {}'.format(primeiro1, ultimo1))