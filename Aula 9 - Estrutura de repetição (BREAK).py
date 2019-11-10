'''O comando break é um comando de interrupção de looping, sua execução faz com que o bloco de execução em loop seja interrompido
e os comandos fora do bloco sejam executados, encerrando o loop. Exemplo:

count = 1
while count <= 10: # se substituir a condição por um 'True' o programa irá rodar para sempre 'looping infinito'. Apena so comando break pode quebrar isto
    print(count)
    count += 1
print('Acabou')'''

count = 1
while True:
    print(count)
    count +=1
    if count == 99:
        break
print('FIM')