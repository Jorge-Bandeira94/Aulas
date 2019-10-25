# Uma cadeia de caracteres ou de texto é uma frase (string), para o python toda cadeia de texto esta entre aspas simples ou duplas

# Atribuit uma string a um valor
frase = 'Curso em Video Python'

#Cada caractere esta guardado em um espaço na memória do computador, os chamados índices, em python
# o primeiro caractere de uma frase é de indice 0, logo no indice 0 estará a letra 'c', no indice 4
# a letra 'o'.

# Técnica de fatiamento (pegando indices alvos na string)
frase[9] # Variavel + [numero]
print(frase[9]) # O décimo caracter da frase 'curso em video'
print(frase[9:13]) # Apresenta todos os caracteres do 9 ao 12, o 13 é excluido
print(frase[9:14])
print(frase[9:21]) # O valor 21 n existe pois a frase só possui 20 caracteres, porém o python consegue entender e ignora o mesmo
print(frase[9:21:2])# Vai retornar a frase do caractere 9 ao 20 porém excluindo um caractere a cada dois
print(frase[:5]) # Quando não se coloca onde vai começar a leitura começa do caracter 0, e ensse caso irá ate o 4
print(frase[15:]) # A leitura vai começar a partir do caractere 15 até o final
print(frase[9::3]) # A leitura irá começar no caractere 9 até o final pulando a cada 3 caracteres

# Análise de strings
len(frase) # descreve o comprimento da frase
print(len(frase))
print(frase.count('o')) #conta quantas vezes existe a letra 'o' na frase
print(frase.count('o',0, 13)) #conta quantos 'o' tem da posição zero até a treze (um fatiamento dentro da análise)
print(frase.find('deo')) #diz em que momento começou o "deo', no caso, na posição 11. Se houver diferenças entre maiusculo e minúsculo o find não conseguirá encontrar o alvo e respodnerá -1
print(frase.find('Android')) #Quando se procura uma string que não existe em outra string retorna-se o valor -1
print('curso' in frase) # O operador in tbm procura se existe uma string em outra string, ele retorna em True ou False

# Transformação
# Uma string é imutável, mas ela pode ser manipulada através de métodos
# O replace não muda a string, é necessário que o replace seja correspondido à variável de forma: frase = frase.replace('Python', 'Android'). Se não for assim o print da frase não mostrara a palavra android no lugar
print(frase.replace('Python', 'Android')) # Substitui python por android
print(frase.upper()) # Transforma os caracteres em maiusculos
print(frase.lower()) # Transforma todos os caracteres em minúsculos
print(frase.capitalize()) # Deixa apenas o primeiro caractere em maiúsculo
print(frase.title()) # Analise quantas palavras tem numa string e depois de cada espaço ele deixa a primeira letra da palavra maiúsucla

frase2 = '   Aprenda Python  '
print(frase2.strip()) # Remove todos os espaços inuteis da string (não inclue os espaços necessarios para separar palavras
print(frase2.rstrip()) # Apenas o lado direito é removido (os espaços)
print(frase2.lstrip()) # Remove os espaços da esquerda e mantém os da direita

# Divisão de strings
print(frase.split()) # Vai ocorre divisões considerando os espaços no string. Cada palavra vai começar do indice 0 criando strings diferentes. É gerada uma lista com indexação tbm para cada palavra, ao invés de caractere
dividido = frase.split() # Dando à uma variável um método para a 'frase'
print(dividido[0]) # Irá retornar a primeira palavra da lista, indexada como 0
print(dividido [2] [3]) # Irá mostrar a letra indexada como 3 na palavra indexada como 2

# Junção de string
print(''.join(frase)) # Junta as palavras de volta podendo escolher quais caracteres irão ser usados entre cada elemento da frase
print('-'.join(frase))

# Uma maneira mais fácil de escrever textos na tela com print, sem precisar usar um print para cada linha, é usando aspas triplas segue como:
print('''Texto é um conjunto de palavras e frases encadeadas 
que permitem interpretação e transmitem uma mensagem. 
É qualquer obra escrita em versão original e que constitui 
um livro ou um documento escrito. Um texto é uma unidade 
linguística de extensão superior à frase''')


