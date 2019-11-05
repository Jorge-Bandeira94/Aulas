'''O loop for criará uma repetição infinita que terminará apenas quando uma condição for saciada
podemos escreve-la da seguinte forma:

for x in x:
    ação
final da ação
'''

#Exemplos
for c in range(0, 5): #o ultimo numero é ignorado
    print('oi')
print('Fim')
print('\n', 20*'-=-')


for c in range(10, 0, -1): # o terceiro numero sendo -1 indica uma contagem descrescente
    print(c)
print('\n', 20*'-=-')


i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range (i, f+1, p): #f+1 por que o ultimo numero é ignorado
    print(c)
print('\n', 20*'-=-')

#repetindo ações
for c in range(0,4): #irá ocorrer de que se eu digita algo que não seja um nuemro o loop continuara por 4 vezes
    a = int(input('Digite um valor'))
print('\n', 20*'-=-')


for c in range(0, 6):
    value = c * 2
    print(value)
    if c == 4:
        print('Parar')
        break




