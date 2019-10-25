# Condições aninhada
# Condições dentro de estruturas condicionais como:

#if x+a:
    #print(a)
#elif x+b:
    #pint(b)
#else:
    #print(c)

#Prática
#condição simples
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome feio!')
print('Tenha um bom dia {}!'.format(nome))

#condição composta
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome feio!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))

#Estrutura condicional alinhada
nome = str(input('Qual é seu nome? ')).capitalize()
if nome == 'Gustavo':
    print('Que nome feio!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular {}!'.format(nome))
elif nome in 'João Pedro Roberto Ana Claudia Patrícia':
    print('Este nome é bem comum no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))



