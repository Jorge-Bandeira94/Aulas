# O código ANSI é um paradigma que está presnete em muitas linguagems, são códigos pré pronto para coisas padronizadas.
# O melhor código para representar cores no python é o 033, neste caso será feito da seguinte forma:
# \033[m, entre o colchete e o 'm' será inserido um código que representará a cor desejada
# \033[estilo (do texto) texto backgorund(cor do fundo) m
#\o33[0;33;44m

''' 
- Códigos para estilo:
0 = Nenhum
1 = Negrito
4 = sublinhado
7 = inverter as cores com o fundo

- Códigos para cor do texto
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = azul claro
37 = cinza

- Códigos para cor do background
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = azul claro
47 = cinza
'''

print('\033[1;31;43mOlá, mundo!\033[m') #O comando no final serve para limitar a coloração do background apenas à frase

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
print('Os valores são \033[36m{}\033[m e \033[32m{}\033[m'.format(a, b))

nome = str(input('Digite seu nome: '))
print('Muito prazer em conhece-lo {}{}{}!'.format('\033[4:36m', nome, '\033[m')) #colocando os comandos de iniciar e finalizar as cores em cada mascara {}