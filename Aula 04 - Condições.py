'''As condições são linhas diferentes de comandos que ocorrem paralelamente e seguem dependendo de uma condição escolhida
Uma bifurcação na estrada faz com que um carro autonomo precise tomar uma decisão entre dois caminhos e dependendo do caminho escolhido,
os comandos futuros serão diferentes. Na programação o comando que diz qual bloco de comandos será utilizado depois de uma escolha é 
'if'. Nestes tipos de comandos serão utilizandos as identações para criar uma hierarquia do tipo. A identação é executada pela TAB

carro.siga()
secarro.esquerda() #condição verdadeira executara estes comandos (Bloco verdadeiro)
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
senão #condição falsa, executara estes comandos (Bloco Falso)
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
carro.pare() # condição que sempre será executada por não estar identada
'''

# No python, esta linguagem é da seguinte forma: 'if carro.esquerda:' e se não: 'else:'
tempo = int(input('Quantos anos tem seu carro?'  ))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--') # sempre será executado por não estar não está identado dentro do bloco

# Condição simplificada
tempo = int(input('Quantos anos tem seu carro?'  ))
print('Carro novo' if tempo<=3 else 'Carro Velho')
print('--Fim--')

# Sem condição falsa 'else'
nome = str(input('Qual o seu nome?' )).strip().lower()
if nome == 'jorge':
    print('Que nome lindo você tem!') # Esse comando só vai acontecer se o nome for 'Jorge', se não, só a mensagem abaixo é exibida
print('Bom dia, {}!'.format(nome.capitalize())) # Sem identação, sempre vai ocorrer

# Adicionando a condição falsa 'else'
nome = str(input('Qual o seu nome?' )).strip().lower() # o método .lower() força a formatação da string para se adequar a condção do if
if nome == 'jorge': # nunca esquecer dos ':' no final do comando de if e else
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome.capitalize())) #Capitalizar para ficar esteticamente mais bonito

# Exemplo com notas de alunos
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7: #nunca esquecer os ':' no final do comando de if e else
    print('O aluno foi aprovado com média {:.2f}'.format(media)) # Bloco verdadeiro
else:
    print('O aluno não foi aprovado, sua média foi {}'.format(media)) # Bloco Falso
print('--FIM--')
