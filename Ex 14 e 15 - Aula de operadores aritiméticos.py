# Calcule o preço de um produto que pago a vista tem 10% de desconto e parcelado tem *% de aumento em cada parcela
prod = float(input('Digite o valor do produto. R$ '))
desconto = prod - (prod * 10 / 100) # esta forma de armar o calculo de porcentagem tbm é valida
acre = (prod * 8 / 100) + prod # Aumento
print('O produto pago a vista irá sair por {:.2f} R$, enquanto que, se parcelado, irá sair por {:.2f} R$'.format(desconto, acre))
print(40 * '=')


#Faça um programa que leia uma temperatura em celsius e retorne em farenheit
c = float(input('Digite uma temperatura: Cº '))
convert = (9 * c) / 5 + 32 # É a fórmula física para conversão destas unidades de temperatura
print('A temperatura em Fº é de {} graus'.format(convert))
print(40 * '=')


#Faça um algoritmo que calcule o alugel de um carro pela quilometragem rodade do mesmo (Na questão original o carro vale 60 por dia e 0.15 por km rodado)
c = float(input('Qual o valor base do alugel? R$ '))
d = int(input('Quantos dias o carro ficará alugado? '))
e = int(input('Qual a taxa em R$ do alugel / dia ? R$ '))
f = float(input('Qual a taxa em R$ para cada 10 Km rodados? R$ '))
g = int(input(' Quantos Km foram rodados ao final do alugel? '))
valor = c + (d * e) + (f * (g / 10))
print('O total à pagar após {} dias e {} Km rodados será {} R$'.format(d, g, valor))
print(40 * '=')


# Respondendo a questão 15
m = int(input('Quantos dias o carro ficou alugado? '))
n = float(input('Quantos quilômetros ele percorreu? '))
taxa = 60 * m + 0.15 * n
print('O valor final do alugel deste carro será de {} R$'.format(taxa))
