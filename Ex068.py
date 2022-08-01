print('\33[1;34m=-\33[m'*20)
print(f'\33[1;35mVAMOS JOGAR PAR OU IMPAR\33[m')
print('\33[1;34m=-\33[m'*20)
from random import randint


cont = soma = 0
while cont == 0:
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    q = input('PAR OU IMPAR? [P|I] ').strip().upper()[0]
    print('\33[1;35m-\33[m'*50)
    if (n + computador) % 2 == 0 and q == 'P':
        print(f'Você jogou {n} e o computador {computador}. Total de {n + computador} DEU PAR')
        print('\33[1;35m-\33[m' * 50)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('\33[1;35m-\33[m' * 50)
        soma += 1
    elif (n + computador) % 2 == 0 and q == 'I':
        print(f'Você jogou {n} e o computador {computador}. Total de {n + computador} DEU PAR')
        print('\33[1;35m-\33[m' * 50)
        print('Você PERDEU!')
        cont += 1
        print('\33[1;35m-\33[m' * 50)
    elif (n + computador) % 2 != 0 and q == 'P':
        print(f'Você jogou {n} e o computador {computador}. Total de {n + computador} DEU IMPAR')
        print('\33[1;35m-\33[m' * 50)
        print('Você PERDEU!')
        cont += 1
        print('\33[1;35m-\33[m' * 50)
    elif (n + computador) % 2 != 0 and q == 'I':
        print(f'Você jogou {n} e o computador {computador}. Total de {n + computador} DEU IMPAR')
        print('\33[1;35m-\33[m' * 50)
        print('Você VENCEU!\nVamos jogar novamente...')
        print('\33[1;35m=\33[m' * 50)
        soma += 1
    if q not in 'PI':
        print('Você digitou algo errado. Tente novamente!')
print('\33[1;34m=-\33[m'*20)
print(f'\33[1;31mGAME OVER!!! Você venceu {soma} vezes')
    #print('\33[1;35m=\33[m' * 20)


### CURSO EM VIDEO


v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo  not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
    elif tipo == 'I':
        if tipo % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!! Você venceu {v} vezes')

