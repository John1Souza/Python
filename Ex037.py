from time import sleep

while True:
    n = float(input('Digite um valor para conversão: '))
    conversão = int(input('Qual será a base de conversão?'
                      '[1] BINÁRIO'
                      '[2] OCTAL'
                      '[3] HEXADECIQMAL '))
    if conversão == 1:
        #CONVERSÃO PARA BINÁRIO
        print('='*12,end=' ')
        print('Convertendo para binário...')
        print('='*12)
        sleep(1)
        bin = n // 2
        if n % 2 != 0:
            bin1 = 1
        elif n % 2 == 0:
            bin1 = 0
        if (bin // 2) % 2 == 0:
            bin2 = 0
        elif (bin // 2) % 2 != 0:
            bin2 = 1








    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break