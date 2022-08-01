from time import  sleep

while True:
    n = int(input('Digite um valor: '))
    print('=' * 10, end=' ')
    print('ANALISANDO...', end=' ')
    print('=' * 10)
    sleep(1)
    if n % 2 == 0:
        print('Seu número é PAR!')
    if n % 2 != 0:
        print('Seu número é ÍMPAR!')
    q = input('Quer continuar? [S/N] ').upper()
    if q == "S":
        continue
    else:
        break
print('-'*20, end=' ')
print('FIM', end=' ')
print('-'*20)