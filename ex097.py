def escreva(msg):
    for i in range(0, len(msg)+4):
        print(f'~', end='')
    print()
    print(f'  {msg}')
    for i in range(0, len(msg)+4):
        print(f'~', end='')





# PROJETO PRINCIPAL
mens = str(input('Digite sua mensagem: '))
escreva(mens)
print()
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')