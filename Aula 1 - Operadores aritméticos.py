'''   Os operadores normalmente utilizados são '+' para adição '-' para subtração, '*' para multiplicação '/' para divisão
'**' para potência, '//' para divisão inteira e '%' para módulo ou resto da divisão.
Antes do Operador aritimético necessita-se do operando, no caso números ou as variáveis que representam os números . Estes operadore são
binários, ou seja, necessitam de outros operandos para concluir a operação, no caso, numeros após os simbolos. Para concluir as operações
são atribuídos dois simbolos de =, pois, quando se usa apenas um, indica-se correspondencia e não resultado.'''

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2 #Divisão sem usar virgulas
5 % 2 == 1 #vALOR QUE SOBRA DA DIVISÃO INTEIRA (vizualizado no quociente)

'''Os operadores possuem ordem de precedência (como na matemática), os primeiros a serem executadas são os numéros dentro dos 
parenteses (podem haver parenteses dentro de parenteses). Após os parenteses, o que se é resolvido em sequência são as potências -> 
a multiplciação, divisão, divisão inteira e resto da divisão -> por último adição e subtração.'''

a = 5
b = 2
S = a + b
print('Adição', S)

a = 5
b = 2
S = a - b
print('Subtração', S)

a = 5
b = 2
S = a / b
print('Divisão', S)

a = 5
b = 2
S = a * b
print('Multiplicação', S)

a = 5
b = 2
S = a ** b
print('Potência', S)

a = 5
b = 2
S = a // b
print('Divisão inteira', S)

a = 5
b = 2
S = a % b
print('Resto da divisão', S)

# Para calcular raíz quadrada basta adicionar a potencia e uma divisão entre parenteses tal como

c = 81
d = c **(1/2) #1/3 para raíz cúbica
print('Raíz quadrada', d)

# É possível operar strings também, exemplos:
print('='*20)
print('Ola'*3)

# Alguns detalhes como a centralização de respostas pode ser útil, para isto segue o exemplo:
nome = input('Qual o seu nome?')
print('Prazer em te conhecer {:>20}!'.format(nome)) #Direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #Esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #Centro
print('Prazer em te conhecer {:=^20}!'.format(nome))

# Agora com números
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
n = n1 * n2
w = n1 / n2
z = n1 ** n2
print('A soma vale {}'.format(n1+n2)) #quando não atribuímos variáveis à operação são casos em que iremos utiliza-los uma ou poucas vezes
print('A soma é {}, o produto é {}, a divisão é {}, e a potência é {}'.format(s, n, w, z)) #Dar variaveis aos resultados auxiliam a usar os mesmos números várias vezes no script

''' Caso queira escolher as casas decimas que serão mostradas, dentro dos {} digitar {:.3f} que significa 3 casas flutuantes, e o número pode ser variavel para quantidade de casas desejadas
A sintaxe com virgulas ou com "+' sao menos poderosas que com {} pois o {} possibilita outras configurações como visto acima. Caso os resultados devam aparecer todos na mesma linha 
(não quebrar linhas) digitar end=' ', tal como:'''

print('A soma vale {}, o produto vale {}, a divisão vale {}, e a potência vale {}'.format(s, n, w, z), end=' ') # O espaço vazio entre as apsas simples do laod de end= significa o que será colocado para juntar as linhas

#De forma similar pode-se quebrar uma linha no meio do print com \n, como:

print('\nA soma vale {}, \no produto vale {}, \na divisão vale {}, \ne a potência vale {}'.format(s, n, w, z), end=' ')
